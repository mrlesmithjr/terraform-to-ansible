"""terraform_to_ansible/__main__.py"""

from terraform_to_ansible.cli import cli_args
from terraform_to_ansible.inventory import Inventory
from terraform_to_ansible.logger import setup_logger
from terraform_to_ansible.parser import Parser


def main():
    """Main execution of package."""

    # Setup root logger
    setup_logger()

    # Capture CLI arguments
    args = cli_args()

    # Parse Terraform tfstate
    parser = Parser(args)
    all_resources = parser.parse()

    # Generate Ansible inventory
    inventory = Inventory(args, all_resources)
    ansible_inventory = inventory.generate()
    # Save Ansible inventory
    inventory.save(ansible_inventory)


if __name__ == "__main__":
    main()
