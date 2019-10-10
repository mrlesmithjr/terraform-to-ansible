# terraform_to_ansible/parsers/azurerm_public_ip.py
"""Parse Azure RM public IPs found in Terraform tfstate."""


class AzureRMpublicIP:
    """Main Azure RM public IP class."""

    def __init__(self, azurerm_public_ips, instances):
        self.azurerm_public_ips = azurerm_public_ips
        self.azurerm_public_ip_instances = instances

    def parse(self):
        """Parse Azure RM public IP instances."""
        for instance in self.azurerm_public_ip_instances:
            attributes = instance.get('attributes')
            self.update(attributes)

    def update(self, attributes):
        """Update Azure RM public IPs found."""
        self.azurerm_public_ips.append(attributes)
