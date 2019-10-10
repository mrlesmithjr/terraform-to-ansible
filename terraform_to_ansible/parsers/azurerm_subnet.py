# terraform_to_ansible/parsers/azurerm_subnet.py
"""Parse Azure RM subnets found in Terraform tfstate."""


class AzureRMsubnet:
    """Main Azure RM subnet class."""

    def __init__(self, azurerm_subnets, instances):
        self.azurerm_subnets = azurerm_subnets
        self.azurerm_subnet_instances = instances

    def parse(self):
        """Parse Azure RM subnet instances."""
        for instance in self.azurerm_subnet_instances:
            attributes = instance.get('attributes')
            self.update(attributes)

    def update(self, attributes):
        """Update Azure RM subnets found."""
        self.azurerm_subnets.append(attributes)
