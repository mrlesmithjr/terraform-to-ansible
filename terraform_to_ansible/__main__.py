# terraform_to_ansible/__main__.py
"""Terraform tfstate to Ansible inventory, etc."""
# import json
import yaml
from terraform_to_ansible.args import get_args
from terraform_to_ansible.parser import Parser
from terraform_to_ansible.inventory import Inventory


def main():
    """Main execution of package."""

    # Capture CLI arguments
    args = get_args()

    # Parse Terraform tfstate
    parser = Parser(args)
    all_resources = parser.parse()

    # Generate Ansible inventory
    inventory = Inventory(all_resources)
    ansible_inventory = inventory.generate()

    # print(json.dumps(all_resources))
    print(yaml.dump(ansible_inventory, indent=4))


if __name__ == '__main__':
    main()
