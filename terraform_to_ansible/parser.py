# terraform_to_ansible/parser.py
"""Parse Terraform tfstate for good stuff."""

import json
import os
import sys


class Parser:
    """Main Terraform tfstate parser."""

    def __init__(self, args):
        """"""
        self.all_resources = dict()

        # Define Terraform tfstate file to load
        self.tfstate = args.tfstate

        # Load Terraform tfstate
        self.load()

        # Capture Terraform version from tfstate
        self.terraform_version = self.data.get('terraform_version')

        # Capture modules to parse
        self.modules = self.data.get('modules')

        # Capture resources to parse
        self.resources = self.data.get('resources')

    def load(self):
        """Load Terraform tfstate file."""
        if os.path.isfile(self.tfstate):
            with open(self.tfstate, 'r') as stream:
                self.data = json.load(stream)
        else:
            print('Error: Terraform tfstate file not found.')
            sys.exit(1)

    def parse(self):
        """Parse Terraform tfstate file."""
        if self.resources is not None:
            for resource in self.resources:
                resource_mode = resource.get('mode')
                if resource_mode == 'managed':
                    resource_type_lookup = self.all_resources.get(
                        resource['type'])
                    if resource_type_lookup is None:
                        self.all_resources[resource['type']] = list()
                    instances = resource.get('instances')
                    if instances is not None:
                        for instance in instances:
                            self.all_resources[resource['type']].append(
                                instance['attributes'])

        if self.modules is not None:
            for module in self.modules:
                resources = module.get('resources')
                if resources is not None:
                    for resource, resource_config in resources.items():
                        resource_type_lookup = self.all_resources.get(
                            resource_config['type'])
                        if resource_type_lookup is None:
                            self.all_resources[resource_config['type']] = list(
                            )
                        self.all_resources[resource_config['type']].append(
                            resource_config['primary']['attributes'])

        return self.all_resources
