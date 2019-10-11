# terraform_to_ansible/parsers/azurerm_virtual_machine.py
"""Parse Azure RM VMs found in Terraform tfstate."""


class AzureRMvirtualMachine:
    """Main Azure RM virtual machine class."""

    def __init__(self, azurerm_virtual_machines, instances):
        self.azurerm_virtual_machines = azurerm_virtual_machines
        self.azurerm_virtual_machine_instances = instances

    def parse(self):
        """Parse Azure RM public IP instances."""
        for instance in self.azurerm_virtual_machine_instances:
            attributes = instance.get('attributes')
            self.update(attributes)

    def update(self, attributes):
        """Update Azure RM public IPs found."""
        self.azurerm_virtual_machines.append(attributes)
