# terraform_to_ansible/parser.py
"""Parse Terraform tfstate for good stuff."""

import json
import sys
import logging


class Parser:
    """Main Terraform tfstate parser."""

    def __init__(self, args):
        """Init a thing."""

        # Define dictionary to hold all parsed resources
        self.all_resources = {}

        # Define Terraform tfstate file to load
        self.tfstate = args.tfstate

        # Setup logging
        self.logger = logging.getLogger(__name__)

    def load(self):
        """Load Terraform tfstate file."""

        try:
            with open(self.tfstate, 'r') as stream:
                data = json.load(stream)

            # Capture Terraform version from tfstate
            # terraform_version = data.get('terraform_version')

            # Capture modules to parse
            modules = data.get('modules')
            if modules is None:
                modules = []

            # Capture resources to parse
            resources = data.get('resources')
            if resources is None:
                resources = []

            return modules, resources

        except FileNotFoundError as error:
            self.logger.error(error)
            sys.exit(1)

    def parse(self):
        """Parse Terraform tfstate file."""

        _modules, resources = self.load()

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

        #     for module in modules:
        #         resources = module.get('resources')
        #         if resources is not None:
        #             for resource, resource_config in resources.items():
        #                 resource_type_lookup = self.all_resources.get(
        #                     resource_config['type'])
        #                 if resource_type_lookup is None:
        #                     self.all_resources[resource_config['type']] = []
        #                 self.all_resources[resource_config['type']].append(
        #                     resource_config['primary']['attributes'])

        return self.all_resources
