# terraform_to_ansible/parsers/azurerm_network_interface.py
"""Parse Azure RM network interfaces found in Terraform tfstate."""


class AzureRMnetworkInterface:
    """Main Azure RM network interface class."""

    def __init__(self, azurerm_network_interfaces, instances):
        self.azurerm_network_interfaces = azurerm_network_interfaces
        self.azurerm_network_interface_instances = instances

    def parse(self):
        """Parse Azure RM public IP instances."""
        for instance in self.azurerm_network_interface_instances:
            attributes = instance.get('attributes')
            self.update(attributes)

    def update(self, attributes):
        """Update Azure RM public IPs found."""
        self.azurerm_network_interfaces.append(attributes)
