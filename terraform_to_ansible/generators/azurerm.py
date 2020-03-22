"""terraform_to_ansible/generators/azurerm.py"""


class AzureRM:
    """Main AzureRM Ansible inventory generator class."""

    def __init__(self, inventory, all_resources, resource_type,
                 resource_config):
        self.inventory = inventory
        self.all_resources = all_resources
        self.resource_type = resource_type
        self.resource_config = resource_config

    def parse(self):
        """Parse Azure RM resources to generate Ansible inventory."""
        self.azurerm_vm()

    def azurerm_vm(self):
        """Main Azure RM virtual machine parsing."""
        nics = self.azurerm_nics()
        pub_ips = self.azurerm_pub_ips()
        inv_res_type_lookup = self.inventory.get(self.resource_type)
        if inv_res_type_lookup is None:
            self.inventory[self.resource_type] = dict(
                children=dict(),
                hosts=dict()
            )
        for virtual_machine in self.resource_config:
            private_ips = set()
            public_ips = set()
            for network_interface_id in virtual_machine[
                    'network_interface_ids']:
                for ip_addr in nics[network_interface_id][
                        'private_ip_addresses']:
                    private_ips.add(ip_addr)
                for ip_config in nics[network_interface_id].get(
                        'ip_configuration'):
                    pub_ip_lookup = pub_ips.get(
                        ip_config['public_ip_address_id'])
                    if pub_ip_lookup is not None:
                        pub_ip = pub_ips[ip_config[
                            'public_ip_address_id']].get('ip_address')
                        public_ips.add(pub_ip)

            vm_info = dict(
                location=virtual_machine['location'],
                os_profile=virtual_machine['os_profile'],
                private_ips=list(private_ips),
                public_ips=list(public_ips),
                resource_group_name=virtual_machine['resource_group_name'],
                storage_image_reference=virtual_machine[
                    'storage_image_reference'],
                tags=virtual_machine['tags'],
                vm_size=virtual_machine['vm_size']
            )
            self.inventory[self.resource_type]['hosts'][
                virtual_machine['name']] = vm_info

    def azurerm_nics(self):
        """
        Parse all resources for Azure RM network interfaces and put into
        dictionary for lookups.
        """
        nics = dict()
        azurerm_network_interfaces = self.all_resources.get(
            'azurerm_network_interface')
        if azurerm_network_interfaces is not None:
            for nic in azurerm_network_interfaces:
                nics[nic['id']] = nic

        return nics

    def azurerm_pub_ips(self):
        """
        Parse all resources for Azure RM public IPs and put into
        dictionary for lookups.
        """
        pub_ips = dict()
        azurerm_public_ips = self.all_resources.get('azurerm_public_ip')
        if azurerm_public_ips is not None:
            for azurerm_public_ip in azurerm_public_ips:
                pub_ips[azurerm_public_ip['id']] = azurerm_public_ip

        return pub_ips
