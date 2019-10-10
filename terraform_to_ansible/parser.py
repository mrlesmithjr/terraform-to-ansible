# terraform_to_ansible/parser.py
"""Parse Terraform tfstate for good stuff."""

import json
import os
import sys
from terraform_to_ansible.resources import resource_types
from terraform_to_ansible.parsers.azurerm import AzureRM


class Parser:
    """Main Terraform tfstate parser."""

    def __init__(self, args):
        """"""
        # Define Terraform tfstate file to load
        self.tfstate = args.tfstate
        self.resource_types = resource_types()
        self.load()

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
                    if resource['provider'] == 'provider.azurerm':
                        azurerm = AzureRM(self.resource_types, resource)
                        azurerm.parse()

        return self.resource_types
