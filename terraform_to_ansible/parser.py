"""terraform_to_ansible/parser.py"""

import json
import logging
import os
import subprocess
import sys


class Parser:
    """Main Terraform tfstate parser."""

    def __init__(self, args):
        """Init a thing."""

        # Define dictionary to hold all parsed resources
        self.all_resources = {}

        # Define Terraform tfstate file to load
        self.tfstate = args.tfstate
        # Define Terraform tfstate directory to load
        self.tfstatedir = args.tfstatedir

        # Setup logging
        self.logger = logging.getLogger(__name__)

    def load(self):
        """Load Terraform tfstate file."""

        # Attempt to load tfstate file directly
        if self.tfstate is not None:
            # Log tfstate file path
            self.logger.info("Loading --tfstate %s", self.tfstate)

            try:
                # Open tfstate file
                with open(self.tfstate, "r") as stream:
                    # Load JSON data
                    try:
                        data = json.load(stream)

                    # Log and exit if JSON data not found
                    except json.JSONDecodeError as error:
                        self.logger.error(error)
                        sys.exit(1)

            # Log and exit if file not found
            except FileNotFoundError as error:
                self.logger.error(error)
                sys.exit(1)

        # Attempt to load tfstate from directory using terraform state pull
        else:
            # Log tfstate directory
            self.logger.info("Loading --tfstatedir %s", self.tfstatedir)

            try:
                # Capture current working directory prior to changing to the
                # tfstate directory. So, we can changing back.
                current_dir = os.getcwd()

                # Change to the tfstate directory
                os.chdir(self.tfstatedir)

                try:
                    # Try to load JSON output from terraform state pull command
                    data = json.loads(subprocess.getoutput("terraform state pull"))

                # Log and exit if JSON data not found
                except json.decoder.JSONDecodeError as error:
                    self.logger.error(error)
                    sys.exit(1)

                # Change back to the original current working directory
                os.chdir(current_dir)

            # Log and exit if file/directory not found
            except FileNotFoundError as error:
                self.logger.error(error)
                sys.exit(1)

        # Capture Terraform version from tfstate
        terraform_version = data.get("terraform_version")

        # Log Terraform version for additional logic if needed. Not used at
        # this time.
        self.logger.info("terraform_version: %s", terraform_version)

        # Capture resources to parse
        resources = data.get("resources")
        if resources is None:
            resources = []
            modules = data.get("modules")
            if modules is not None:
                resources = modules[0].get("resources")

        return resources

    def parse(self):
        """Parse Terraform tfstate file."""

        # Load resources up
        resources = self.load()

        # Check if resources are a list - newer Terraform versions
        if isinstance(resources, list):
            for resource in resources:
                self.resource_types(resource)

                instances = resource.get("instances")
                if instances is not None:
                    for instance in instances:
                        self.all_resources[resource["type"]].append(
                            instance["attributes"]
                        )

        # Check if resources are a dict - older Terraform versions
        elif isinstance(resources, dict):
            for resource, resource_config in resources.items():
                self.resource_types(resource_config)
                self.all_resources[resource_config["type"]].append(
                    resource_config["primary"]["attributes"]
                )

        return self.all_resources

    def resource_types(self, resource):
        """Populate resource types."""

        # Check to see if all_resources is already populated with resource type
        resource_type_lookup = self.all_resources.get(resource["type"])

        # Add resource type to all resources if not found in lookup
        if resource_type_lookup is None:
            self.all_resources[resource["type"]] = []
