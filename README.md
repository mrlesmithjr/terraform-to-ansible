# python-terraform-to-ansible

Consume Terraform tfstate and generate usable Ansible inventory.

## Usage

### Help

````bash
python -m terraform_to_ansible --help
...
usage: __main__.py [-h] [--inventory INVENTORY] [--tfstate TFSTATE]
                   [--version]

optional arguments:
  -h, --help            show this help message and exit
  --inventory INVENTORY
                        File to save Ansible inventory as
  --tfstate TFSTATE     Terraform tftstate file to parse
  --version             show program's version number and exit
```

### Parsing

```bash
python -m terraform_to_ansible --tfstate terraform.tfstate.azure
````
