---
title: Terraform to Ansible Usage
---

## Help

To display help simply execute:

```bash
python -m terraform_to_ansible --help
...
usage: __main__.py [-h] [--ansibleHost {private,public}] [--force]
                   [--output OUTPUT] [--format {json,yaml}]
                   [--tfstate TFSTATE] [--tfstatedir TFSTATEDIR] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --ansibleHost {private,public}
                        Use private or public IPs
  --force               Force overwrite
  --output OUTPUT       Output file to save Ansible inventory to
  --format {json,yaml}  Format to output inventory as
  --tfstate TFSTATE     Terraform tftstate file to parse
  --tfstatedir TFSTATEDIR
                        Terraform tftstate dir to parse
  --version             show program's version number and exit
```

## Displaying to Stdout

By default, after loading your [TFState Inputs](#tfstate-inputs), the inventory
will be displayed to Stdout only.

## Output Format

Currently JSON and YAML formatting are supported. The default output format is
YAML. However, you can control whether to display in either format by:

```bash
python -m terraform_to_ansible --tfstate terraform.tfstate --format {json,yaml}
```

## TFState Inputs

There are several ways in which to load your tfstate data.

- [Load file](#load-file)
- [Load directory](#load-directory)

### Load File

To load a tfstate file directly execute the following:

```bash
python -m terraform_to_ansible --tfstate terraform.tfstate
```

### Load Directory

For cases in which your tfstate is remote, you can simply do the following to load
the directory where you execute Terraform from:

```bash
python -m terraform_to_ansible --tfstatedir ~/Projects/Terraform/Example
```

## Saving Inventory

In order to save the generated Ansible inventory, simply provide the `--output`
argument and location to save to. If an existing file already exists with the
same name, you will get an error. You can pass the `--force` argument to overwrite
the existing file. Again, the default will be YAML, but you can also save as
JSON if needed.

## Tagging

Best practices are to use tags for your resources when provisioning. We will use
tags found, to generate Ansible groupings.
