# terraform_to_ansible/parsers/azurerm.py
"""Parse Azure RM resources found in Terraform tfstate."""

from terraform_to_ansible.parsers.azurerm_public_ip import AzureRMpublicIP
from terraform_to_ansible.parsers.azurerm_subnet import AzureRMsubnet
from terraform_to_ansible.parsers.azurerm_virtual_machine import AzureRMvirtualMachine
from terraform_to_ansible.parsers.azurerm_network_interface import AzureRMnetworkInterface


class AzureRM:
    """Main Azure RM parser class."""

    def __init__(self, resource_types, resource):
        """"""
        self.resource = resource
        self.resource_instances = self.resource.get('instances')
        self.azurerm_public_ips = resource_types['azurerm_public_ips']
        self.azurerm_subnets = resource_types['azurerm_subnets']
        self.azurerm_vms = resource_types['azurerm_virtual_machines']
        self.azurerm_nics = resource_types['azurerm_network_interfaces']

    def parse(self):
        """Main Azure RM parser function."""
        resource_type = self.resource.get('type')

        if resource_type == 'azurerm_public_ip':
            self.public_ips()

        elif resource_type == 'azurerm_subnet':
            self.subnets()

        elif resource_type == 'azurerm_virtual_machine':
            self.vms()

        elif resource_type == 'azurerm_network_interface':
            self.nics()

    def public_ips(self):
        """Parse Azure RM public IPs."""
        azure_rm_pub_ip = AzureRMpublicIP(
            self.azurerm_public_ips, self.resource_instances)
        azure_rm_pub_ip.parse()

    def subnets(self):
        """Parse Azure RM subnets."""
        azure_rm_subnet = AzureRMsubnet(
            self.azurerm_subnets, self.resource_instances)
        azure_rm_subnet.parse()

    def vms(self):
        """Parse Azure RM VMs."""
        azure_vm = AzureRMvirtualMachine(
            self.azurerm_vms, self.resource_instances)
        azure_vm.parse()

    def nics(self):
        """Parse Azure RM network interfaces."""
        azure_nic = AzureRMnetworkInterface(
            self.azurerm_nics, self.resource_instances)
        azure_nic.parse()
