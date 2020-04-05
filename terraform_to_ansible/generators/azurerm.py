"""terraform_to_ansible/generators/azurerm.py"""

import logging


class AzureRM:
    """Main AzureRM Ansible inventory generator class."""

    def __init__(self, **kwargs):
        # Define whether private or public ip for ansible_host
        self.ansible_host = kwargs['data']['ansible_host']
        self.inventory = kwargs['data']['inventory']
        self.all_resources = kwargs['data']['all_resources']
        self.resource_type = kwargs['data']['resource_type']
        self.resource_config = kwargs['data']['resource_config']

        # Setup logging
        self.logger = logging.getLogger(__name__)

    def parse(self):
        """Parse Azure RM resources to generate Ansible inventory."""
        # self.azurerm_vm()

        # Lookup AzureRM inventory group
        lookup = self.inventory['all']['children'].get('AzureRM')
        # Add AzureRM inventory group if it does not exist
        if lookup is None:
            self.inventory['all']['children']['AzureRM'] = {
                'hosts': {}, 'vars': {}}

        # Log resource type
        self.logger.info('resource_type: %s', self.resource_type)
        # Log resource config
        self.logger.info('resource_config: %s', self.resource_config)

        # Define resource mappings to functions
        resource_map = {'azurerm_virtual_machine': self.virtual_machine,
                        'azurerm_linux_virtual_machine': self.virtual_machine,
                        'azurerm_network_interface': self.network_interface,
                        'azurerm_public_ip': self.public_ip,
                        'azurerm_resource_group': self.resource_group,
                        'azurerm_virtual_network': self.virtual_network,
                        'azurerm_subnet': self.subnet}

        try:
            # Lookup resource mapping
            resource = resource_map[self.resource_type]
            # Execute function based on mapping
            resource()
        except KeyError as error:
            self.logger.error(error)

    def virtual_machine(self):
        """Parse AzureRM virtual machine resources"""

        # Define VM name from resource config
        vm_name = self.resource_config['name']
        self.inventory['all']['children']['AzureRM']['hosts'][
            vm_name] = self.resource_config

        if self.ansible_host == 'private':
            ansible_host = self.resource_config['private_ip_address']
        else:
            ansible_host = self.resource_config['public_ip_address']

        self.inventory['all']['children']['AzureRM']['hosts'][
            vm_name]['ansible_host'] = ansible_host
        self.inventory['all']['children']['AzureRM']['hosts'][
            vm_name]['ansible_user'] = self.resource_config['admin_username']
        for _key, value in self.resource_config['tags'].items():
            # Convert tag to underscore to ensure no issues with - in tags
            tag = value.replace('-', '_')
            tag_lookup = self.inventory['all']['children'].get(tag)
            if tag_lookup is None:
                self.inventory['all']['children'][tag] = {
                    'hosts': {}, 'vars': {}, 'children': {}}
            self.inventory['all']['children'][tag]['hosts'][vm_name] = {}

    def network_interface(self):
        """Parse AzureRM network interface resources"""

    def public_ip(self):
        """Parse AzureRM public IP resources"""

    def resource_group(self):
        """Parse AzureRM resource groups"""

    def virtual_network(self):
        """Parse AzureRM virtual network resources"""

    def subnet(self):
        """Parse AzureRM subnet resources"""
