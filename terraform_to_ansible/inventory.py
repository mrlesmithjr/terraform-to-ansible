# terraform_to_ansible/inventory.py
"""Translate Terraform tfstate to Ansible inventory."""
from terraform_to_ansible.generators.azurerm import AzureRM


class Inventory:
    """Main Ansible inventory class."""

    def __init__(self, all_resources):
        self.all_resources = all_resources
        self.inventory = dict()

    def generate(self):
        """Generate Ansible inventory for consumption."""
        for resource_type, resource_config in self.all_resources.items():
            if resource_type == 'azurerm_virtual_machine':
                azurerm = AzureRM(
                    self.inventory, self.all_resources, resource_type,
                    resource_config)
                azurerm.parse()

        return self.inventory

    def save(self):
        """Save Ansible inventory to yaml."""
