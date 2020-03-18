# terraform_to_ansible/parser.py
"""Parse Terraform tfstate for good stuff."""

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
            try:
                with open(self.tfstate, 'r') as stream:
                    data = json.load(stream)

            except FileNotFoundError as error:
                self.logger.error(error)
                sys.exit(1)

        # Attempt to load tfstate from directory using terraform state pull
        else:
            try:
                current_dir = os.getcwd()
                os.chdir(self.tfstatedir)
                data = json.loads(subprocess.getoutput('terraform state pull'))
                os.chdir(current_dir)

            except FileNotFoundError as error:
                self.logger.error(error)
                sys.exit(1)

        # Capture Terraform version from tfstate
        terraform_version = data.get('terraform_version')
        self.logger.info('terraform_version: %s', terraform_version)

        # Capture resources to parse
        resources = data.get('resources')
        if resources is None:
            resources = []

        return resources

    def parse(self):
        """Parse Terraform tfstate file."""

        resources = self.load()

        for resource in resources:
            resource_mode = resource.get('mode')
            if resource_mode == 'managed':
                resource_type_lookup = self.all_resources.get(
                    resource['type'])
                if resource_type_lookup is None:
                    self.all_resources[resource['type']] = []
                instances = resource.get('instances')
                if instances is not None:
                    for instance in instances:
                        self.all_resources[resource['type']].append(
                            instance['attributes'])

        return self.all_resources
