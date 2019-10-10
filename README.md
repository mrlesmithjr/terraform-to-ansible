# python-terraform-to-ansible

Consume Terraform tfstate and generate usable Ansible inventory.

## Usage

### Help

```bash
python -m terraform_to_ansible --help
...
usage: __main__.py [-h] [--backend {local,consul}] [--consulHost CONSULHOST]
                   [--consulKV CONSULKV] [--consulPort CONSULPORT]
                   [--consulScheme {http,https}] [--inventory INVENTORY]
                   [--logLevel {CRITICAL,ERROR,WARNING,INFO,DEBUG}]
                   [--tfstate TFSTATE] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --backend {local,consul}
                        Define which Terraform backend to parse
  --consulHost CONSULHOST
                        Define Consul host when using Consul backend
  --consulKV CONSULKV   Define Consul KV Pair to query. Ex. Azure/Test
  --consulPort CONSULPORT
                        Define Consul host port
  --consulScheme {http,https}
                        Define Consul connection scheme.
  --inventory INVENTORY
                        Ansible inventory
  --logLevel {CRITICAL,ERROR,WARNING,INFO,DEBUG}
                        Define logging level output
  --tfstate TFSTATE     Terraform tftstate file
  --version             show program's version number and exit
```

### Parsing

```bash
python -m terraform_to_ansible --tfstate terraform.tfstate.azure
```
