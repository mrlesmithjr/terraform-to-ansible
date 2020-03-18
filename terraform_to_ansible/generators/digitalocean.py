"""Provides main DigitalOcean Class."""
import logging


class DigitalOcean:
    """Main DigitalOcean Class."""

    def __init__(self, **kwargs):
        """Init a thing."""

        # Define whether private or public ip for ansible_host
        self.ansible_host = kwargs['data'].get('ansible_host')
        self.inventory = kwargs['data'].get('inventory')
        self.all_resources = kwargs['data'].get('all_resources')
        self.resource_type = kwargs['data'].get('resource_type')
        self.resource_config = kwargs['data'].get('resource_config')

        # Setup logging
        self.logger = logging.getLogger(__name__)

    def parse(self):
        """Parse DigitalOcean resources to generate Ansible inventory."""

        # Lookup DigitalOcean inventory group
        lookup = self.inventory['all']['children'].get('DigitalOcean')
        # Add DigitalOcean inventory group if it does not exist
        if lookup is None:
            self.inventory['all']['children']['DigitalOcean'] = {
                'hosts': {}, 'vars': {}}

        # Log resource type
        self.logger.info('resource_type: %s', self.resource_type)
        # Log resource config
        self.logger.info('resource_config: %s', self.resource_config)

        # Define resource mappings to functions
        resource_map = {'digitalocean_droplet': self.droplet,
                        'digitalocean_firewall': self.firewall,
                        'digitalocean_project': self.project,
                        'digitalocean_domain': self.domain,
                        'digitalocean_record': self.record,
                        'digitalocean_ssh_key': self.ssh_key,
                        'digitalocean_tag': self.tag}

        try:
            # Lookup resource mapping
            resource = resource_map[self.resource_type]
            # Execute function based on mapping
            resource()
        except KeyError as error:
            self.logger.error(error)

    def domain(self):
        """Parse DigitalOcean domain resources."""

        # Lookup DigitalOcean vars domains
        lookup = self.inventory['all']['children']['DigitalOcean']['vars'].get(
            'domains')
        # Add DigitialOcean vars domains if it does not exist
        if lookup is None:
            self.inventory['all']['children']['DigitalOcean']['vars'][
                'domains'] = {}
        # Add DigitalOcean domain info
        self.inventory['all']['children']['DigitalOcean']['vars'][
            'domains'][self.resource_config['name']] = self.resource_config

    def droplet(self):
        """Parse DigitalOcean droplet resources."""

        # Define droplet name from resource config
        droplet_name = self.resource_config['name']
        self.inventory['all']['children']['DigitalOcean']['hosts'][
            droplet_name] = self.resource_config

        if self.ansible_host == 'private':
            ansible_host = self.resource_config['ipv4_address_private']
        else:
            ansible_host = self.resource_config['ipv4_address']

        self.inventory['all']['children']['DigitalOcean']['hosts'][
            droplet_name]['ansible_host'] = ansible_host
        self.inventory['all']['children']['DigitalOcean']['hosts'][
            droplet_name]['ansible_user'] = 'root'
        for tag in self.resource_config['tags']:
            tag_lookup = self.inventory['all']['children'].get(tag)
            if tag_lookup is None:
                self.inventory['all']['children'][tag] = {
                    'hosts': {}, 'vars': {}, 'children': {}}
            self.inventory['all']['children'][tag]['hosts'][droplet_name] = {}

    def firewall(self):
        """Parse DigitalOcean firewall resources."""

        # Lookup DigitalOcean vars firewalls
        lookup = self.inventory['all']['children']['DigitalOcean']['vars'].get(
            'firewalls')
        # Add DigitialOcean vars firewalls if it does not exist
        if lookup is None:
            self.inventory['all']['children']['DigitalOcean']['vars'][
                'firewalls'] = {}
        # Add DigitalOcean firewall info
        self.inventory['all']['children']['DigitalOcean']['vars'][
            'firewalls'][self.resource_config['name']] = self.resource_config

    def project(self):
        """Parse DigitalOcean project resources."""

        # Lookup DigitalOcean vars projects
        lookup = self.inventory['all']['children']['DigitalOcean']['vars'].get(
            'projects')
        # Add DigitialOcean vars projects if it does not exist
        if lookup is None:
            self.inventory['all']['children']['DigitalOcean']['vars'][
                'projects'] = {}
        # Add DigitalOcean project info
        self.inventory['all']['children']['DigitalOcean']['vars'][
            'projects'][self.resource_config['name']] = self.resource_config

    def record(self):
        """Parse DigitalOcean DNS record resources."""

        # Lookup DigitalOcean vars records
        lookup = self.inventory['all']['children']['DigitalOcean']['vars'].get(
            'records')
        # Add DigitialOcean vars records if it does not exist
        if lookup is None:
            self.inventory['all']['children']['DigitalOcean']['vars'][
                'records'] = {}
        # Add DigitalOcean record info
        self.inventory['all']['children']['DigitalOcean']['vars'][
            'records'][self.resource_config['name']] = self.resource_config

    def ssh_key(self):
        """Parse DigitalOcean SSH key resources."""

        # Lookup DigitalOcean vars ssh_keys
        lookup = self.inventory['all']['children']['DigitalOcean']['vars'].get(
            'ssh_keys')
        # Add DigitalOcean vars ssh_keys if it does not exist
        if lookup is None:
            self.inventory['all']['children']['DigitalOcean']['vars'][
                'ssh_keys'] = {}
        # Add DigitalOcean ssh_key info
        self.inventory['all']['children']['DigitalOcean']['vars'][
            'ssh_keys'][self.resource_config['name']] = self.resource_config

    def tag(self):
        """Parse DigitalOcean tag resources."""

        # Define tag name from resource config
        tag_name = self.resource_config['name']
        # Lookup DigitalOcean[tag_name] group
        lookup = self.inventory['all']['children'].get(tag_name)
        # Add DigitalOcean[tag_name] group if it does not exist
        if lookup is None:
            self.inventory['all']['children'][tag_name] = {
                'hosts': {}, 'vars': {}, 'children': {}}
