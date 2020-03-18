# terraform_to_ansible/inventory.py
"""Translate Terraform tfstate to Ansible inventory."""

import json
import logging
import os
import yaml
# from terraform_to_ansible.generators.azurerm import AzureRM
from terraform_to_ansible.generators.digitalocean import DigitalOcean
from terraform_to_ansible.generators.vmware import VMware


class Inventory:
    """Main Ansible inventory class."""

    def __init__(self, args, all_resources):
        """Init a thing."""

        self.all_resources = all_resources
        # Define whether private or public ip for ansible_host
        self.ansible_host = args.ansibleHost
        # Define format to present inventory - JSON or YAML
        self.format = args.format
        # Define output file to save inventory to or display to stdout
        self.output = args.output
        # Define force argument
        self.force = args.force
        # Setup logging
        self.logger = logging.getLogger(__name__)

    def generate(self):
        """Generate Ansible inventory for consumption."""

        inventory = {'all': {'children': {}}}
        for resource_type, resource_configs in self.all_resources.items():
            self.logger.info('resource_type: %s', resource_type)

            resource_type_map = {'azurerm': self.azurerm,
                                 'digitalocean': self.digitalocean,
                                 'vmware': self.vmware}

            if 'azurerm' in resource_type:
                resource_mapping = 'azurerm'

            elif 'digitalocean' in resource_type:
                resource_mapping = 'digitalocean'

            elif 'vsphere' in resource_type:
                resource_mapping = 'vmware'

            else:
                pass

            # Lookup resource mapping
            resource = resource_type_map[resource_mapping]
            # Execute function based on mapping
            resource(inventory, resource_type, resource_configs)

        return inventory

    def azurerm(self, inventory, resource_type, resource_configs):
        """Generates AzureRM resources."""

        # Need to revisit AzureRM resources
        # azurerm = AzureRM(
        #     self.inventory, self.all_resources, resource_type,
        #     resource_config)
        # azurerm.parse()

    def digitalocean(self, inventory, resource_type, resource_configs):
        """Generates DigitalOcean resources."""

        for resource_config in resource_configs:
            self.logger.info('resource_config: %s', resource_config)

            # Define data to pass to class
            data = {'inventory': inventory,
                    'all_resources': self.all_resources,
                    'resource_type': resource_type,
                    'resource_config': resource_config,
                    'ansible_host': self.ansible_host}

            digitalocean = DigitalOcean(data=data)
            digitalocean.parse()

    def vmware(self, inventory, resource_type, resource_configs):
        """Generates VMware resources."""

        for resource_config in resource_configs:
            self.logger.info('resource_config: %s', resource_config)

            # Define data to pass to class
            data = {'inventory': inventory,
                    'all_resources': self.all_resources,
                    'resource_type': resource_type,
                    'resource_config': resource_config,
                    'ansible_host': self.ansible_host}

            vmware = VMware(data=data)
            vmware.parse()

    def save(self, ansible_inventory):
        """Save inventory as JSON or YAML."""

        format_map = {'json': self.format_json, 'yaml': self.format_yaml}
        format_mapping = format_map[self.format]
        formatted_inventory = format_mapping(ansible_inventory)

        if self.output is None:
            # Display to stdout only
            self.stdout_only(formatted_inventory)

        else:
            output_map = {'json': self.save_json, 'yaml': self.save_yaml}
            output_mapping = output_map[self.format]

            if os.path.isfile(self.output):
                if self.force:
                    self.logger.info(
                        'Inventory file: %s already exists!', self.output)
                    self.logger.warning(
                        '--force used. Overwriting %s.', self.output)
                    self.logger.info('Saving inventory to %s', self.output)
                    output_mapping(formatted_inventory)
                    self.logger.info(
                        'Successfully saved inventory to %s', self.output)
                else:
                    self.logger.error(
                        'Inventory file: %s already exists!', self.output)
                    self.logger.info('Use --force to overwrite.')

            else:
                self.logger.info('Saving inventory to %s', self.output)
                output_mapping(formatted_inventory)
                self.logger.info(
                    'Successfully saved inventory to %s', self.output)

    def save_json(self, formatted_inventory):
        """Save inventory as JSON."""

        with open(self.output, 'w') as inventory:
            json.dump(json.loads(formatted_inventory), inventory, indent=4)

    def save_yaml(self, formatted_inventory):
        """Save inventory as YAML."""

        with open(self.output, 'w') as inventory:
            inventory.write(formatted_inventory)

    def stdout_only(self, formatted_inventory):
        """Display inventory to stdout only."""

        self.logger.info('Displaying inventory to stdout')
        print(formatted_inventory)

    def format_json(self, ansible_inventory):
        """Format inventory as JSON."""

        self.logger.info('Formatting inventory as JSON')
        json_inventory = json.dumps(ansible_inventory)

        return json_inventory

    def format_yaml(self, ansible_inventory):
        """Format inventory as YAML."""

        self.logger.info('Formatting inventory as YAML')
        yaml_inventory = yaml.dump(ansible_inventory)

        return yaml_inventory
