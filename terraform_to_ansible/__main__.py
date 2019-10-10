# terraform_to_ansible/__main__.py
"""Terraform tfstate to Ansible inventory, etc."""
import json
from terraform_to_ansible.args import get_args
from terraform_to_ansible.parser import Parser


def main():
    """Main execution of package."""

    # Capture CLI arguments
    args = get_args()

    # Parse Terraform tfstate
    parser = Parser(args)
    all_resources = parser.parse()

    print(json.dumps(all_resources))


if __name__ == '__main__':
    main()
