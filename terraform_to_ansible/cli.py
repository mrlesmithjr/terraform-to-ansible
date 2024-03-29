"""terraform_to_ansible/cli.py"""

import argparse
from terraform_to_ansible.release import __package_name__, __version__


def cli_args():
    """Console script for terraform_to_ansible."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ansibleHost",
        help="Use private or public IPs",
        choices=["private", "public"],
        default=None,
    )
    # parser.add_argument('--backend',
    #                     help='Define which Terraform backend to parse',
    #                     choices=['local', 'consul'], default='local')
    # parser.add_argument('--consulHost',
    #                     help='Define Consul host when using Consul backend')
    # parser.add_argument(
    #     '--consulKV',
    #     help='Define Consul KV Pair to query. Ex. Azure/Test')
    # parser.add_argument('--consulPort',
    #                     help='Define Consul host port', default='8500')
    # parser.add_argument('--consulScheme',
    #                     help='Define Consul connection scheme.',
    #                     choices=['http', 'https'], default='http')
    parser.add_argument("--force", help="Force overwrite", action="store_true")
    parser.add_argument(
        "--output", help="Output file to save Ansible inventory to"
    )
    # parser.add_argument('--logLevel', help='Define logging level output',
    #                     choices=['CRITICAL', 'ERROR', 'WARNING',
    #                              'INFO', 'DEBUG'], default='INFO')
    parser.add_argument(
        "--format",
        help="Format to output inventory as",
        choices=["json", "yaml"],
        default="yaml",
    )
    parser.add_argument("--tfstate", help="Terraform tftstate file to parse")
    parser.add_argument("--tfstatedir", help="Terraform tftstate dir to parse")
    parser.add_argument(
        "--version",
        action="version",
        version=f"{__package_name__} {__version__}",
    )
    args = parser.parse_args()
    if args.tfstate is None and args.tfstatedir is None:
        parser.error("--tfstate or --tfstatedir are required!")
    # if args.backend == 'consul' and args.consulHost is None:
    #     parser.error('Consul host is required when using Consul backend.')
    # if args.backend == 'consul' and args.consulKV is None:
    #     parser.error('Consul KV pair is required when using Consul backend')

    return args
