"""Provides main VMware Class."""
import logging


class VMware:
    """Main VMware Class."""

    def __init__(self, inventory, all_resources, resource_type,
                 resource_config, ansible_host):
        """Init a thing."""

        # Define whether private or public ip for ansible_host
        self.ansible_host = ansible_host
        self.inventory = inventory
        self.all_resources = all_resources
        self.resource_type = resource_type
        self.resource_config = resource_config
        # Setup logging
        self.logger = logging.getLogger(__name__)

    def parse(self):
        """Parse VMware resources to generate Ansible inventory."""

        # Lookup VMware inventory group
        lookup = self.inventory['all']['children'].get('VMware')
        # Add VMware inventory group if it does not exist
        if lookup is None:
            self.inventory['all']['children']['VMware'] = {
                'hosts': {}, 'vars': {}}

        # Log resource type
        self.logger.info('resource_type: %s', self.resource_type)
        # Log resource config
        self.logger.info('resource_config: %s', self.resource_config)

        # Define resource mappings to functions
        resource_map = {'dns_a_record_set': self.record,
                        'vsphere_datacenter': self.datacenter,
                        'vsphere_virtual_machine': self.virtual_machine}

        try:
            # Lookup resource mapping
            resource = resource_map[self.resource_type]
            # Execute function based on mapping
            resource()

        except KeyError as error:
            # Log error
            self.logger.error(error)

    def datacenter(self):
        """Parse vSphere datacenter resources."""

        # Lookup vsphere vars datacenters
        lookup = self.inventory['all']['children']['VMware']['vars'].get(
            'datacenters')
        # Add VMware vars datacenters if it does not exist
        if lookup is None:
            self.inventory['all']['children']['VMware']['vars'][
                'datacenters'] = {}
        # Add VMware datacenter info
        self.inventory['all']['children']['VMware']['vars'][
            'datacenters'][self.resource_config['name']] = self.resource_config

    def virtual_machine(self):
        """Parse vSphere virtual machine resources."""

        # Define vm name from resource config
        vm_name = self.resource_config['name']
        self.inventory['all']['children']['VMware']['hosts'][
            vm_name] = self.resource_config

        # Get interface 0, if it is not found ansible_host will be None. Which
        # we can figure out a better way to handle later.
        ansible_host = self.resource_config.get(
            'network_interface.0.ipv4_address')

        # Set ansible_host
        self.inventory['all']['children']['VMware']['hosts'][
            vm_name]['ansible_host'] = ansible_host

        # Need to get some examples of tags to properly create groups
        # for tag in self.resource_config['tags']:
        #     tag_lookup = self.inventory['all']['children'].get(tag)
        #     if tag_lookup is None:
        #         self.inventory['all']['children'][tag] = {
        #             'hosts': {}, 'vars': {}, 'children': {}}
        #     self.inventory['all']['children'][tag]['hosts'][droplet_name] = {}

    def record(self):
        """Parse vSphere DNS record resources."""

        # Lookup vSphere vars records
        lookup = self.inventory['all']['children']['VMware']['vars'].get(
            'records')

        # Add VMware vars records if it does not exist
        if lookup is None:
            self.inventory['all']['children']['VMware']['vars'][
                'records'] = {}

        # Add VMware record info
        self.inventory['all']['children']['VMware']['vars'][
            'records'][self.resource_config['name']] = self.resource_config
