"""terraform_to_ansible/generators/vmware.py"""

import logging


class VMware:
    """Main VMware Class."""

    def __init__(self, **kwargs):
        """Init a thing."""

        # Define whether private or public ip for ansible_host
        self.ansible_host = kwargs["data"]["ansible_host"]
        self.inventory = kwargs["data"]["inventory"]
        self.all_resources = kwargs["data"]["all_resources"]
        self.resource_type = kwargs["data"]["resource_type"]
        self.resource_config = kwargs["data"]["resource_config"]

        # Setup logging
        self.logger = logging.getLogger(__name__)

    def parse(self):
        """Parse VMware resources to generate Ansible inventory."""

        # Lookup VMware inventory group
        lookup = self.inventory["all"]["children"].get("VMware")
        # Add VMware inventory group if it does not exist
        if lookup is None:
            self.inventory["all"]["children"]["VMware"] = {"hosts": {}, "vars": {}}

        # Log resource type
        self.logger.info("resource_type: %s", self.resource_type)
        # Log resource config
        self.logger.info("resource_config: %s", self.resource_config)

        # Define resource mappings to functions
        resource_map = {
            "dns_a_record_set": self.record,
            "vsphere_datacenter": self.datacenter,
            "vsphere_tag": self.tag,
            "vsphere_virtual_machine": self.virtual_machine,
        }

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
        lookup = self.inventory["all"]["children"]["VMware"]["vars"].get("datacenters")
        # Add VMware vars datacenters if it does not exist
        if lookup is None:
            self.inventory["all"]["children"]["VMware"]["vars"]["datacenters"] = {}
        # Add VMware datacenter info
        self.inventory["all"]["children"]["VMware"]["vars"]["datacenters"][
            self.resource_config["name"]
        ] = self.resource_config

    def tag(self):
        """Parse vSphere tags."""

        # Lookup vsphere vars tags
        lookup = self.inventory["all"]["children"]["VMware"]["vars"].get("tags")
        # Add VMware vars tags if it does not exist
        if lookup is None:
            self.inventory["all"]["children"]["VMware"]["vars"]["tags"] = {}
        # Define tag name from resource config
        tag_name = self.resource_config["name"].replace("-", "_")
        # Add VMware tag into
        self.inventory["all"]["children"]["VMware"]["vars"]["tags"][
            self.resource_config["id"]
        ] = tag_name

        # Lookup VMware[tag_name] group
        lookup = self.inventory["all"]["children"].get(tag_name)
        # Add VMware[tag_name] group if it does not exist
        if lookup is None:
            self.inventory["all"]["children"][tag_name] = {
                "hosts": {},
                "vars": {},
                "children": {},
            }

    def virtual_machine(self):
        """Parse vSphere virtual machine resources."""

        # Check to ensure not a template and has a default IP address
        ansible_host = self.resource_config.get("default_ip_address")

        # Only add if ansible_host is not null
        if ansible_host is not None:
            # Define vm name from resource config
            vm_name = self.resource_config["name"]
            self.inventory["all"]["children"]["VMware"]["hosts"][
                vm_name
            ] = self.resource_config

            # Set ansible_host
            self.inventory["all"]["children"]["VMware"]["hosts"][vm_name][
                "ansible_host"
            ] = ansible_host

    def record(self):
        """Parse vSphere DNS record resources."""

        # Lookup vSphere vars records
        lookup = self.inventory["all"]["children"]["VMware"]["vars"].get("records")

        # Add VMware vars records if it does not exist
        if lookup is None:
            self.inventory["all"]["children"]["VMware"]["vars"]["records"] = {}

        # Add VMware record info
        self.inventory["all"]["children"]["VMware"]["vars"]["records"][
            self.resource_config["name"]
        ] = self.resource_config
