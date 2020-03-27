# Terraform to Ansible Usage

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

> NOTE: Tags with `-` in them will be converted to `_` to fall within Ansible
> standards for groups.

## Examples

### Example Stdout - Default (YAML)

```bash
python -m terraform_to_ansible --tfstatedir Deployment/Terraform/example
```

```yaml
all:
  children:
    DigitalOcean:
      hosts:
        test-01:
          ansible_host: 192.245.252.9
          ansible_user: root
          backups: false
          created_at: "2020-03-18T04:10:53Z"
          disk: 50
          id: ""
          image: ubuntu-18-04-x64
          ipv4_address: 192.245.252.9
          ipv4_address_private: 10.136.185.151
          ipv6: false
          ipv6_address: ""
          ipv6_address_private: null
          locked: false
          memory: 2048
          monitoring: false
          name: test-01
          price_hourly: 0.01488
          price_monthly: 10
          private_networking: true
          region: nyc1
          resize_disk: true
          size: s-1vcpu-2gb
          ssh_keys:
            - ""
          status: active
          tags:
            - test
          urn: do:droplet:185238864
          user_data: null
          vcpus: 1
          volume_ids: []
      vars:
        projects:
          TerraformCloud:
            created_at: "2020-03-18T04:04:29Z"
            description: Terraform Cloud Project
            environment: Development
            id: ""
            name: TerraformCloud
            owner_id: ""
            owner_uuid: ""
            purpose: Terraform Cloud Project
            resources:
              - do:droplet:185238864
            updated_at: "2020-03-18T04:04:29Z"
    test:
      children: {}
      hosts:
        test-01: {}
      vars: {}
```

### Example Stdout - JSON

```bash
python -m terraform_to_ansible --tfstatedir Deployment/Terraform/example --format json | jq
```

```json
{
  "all": {
    "children": {
      "DigitalOcean": {
        "hosts": {
          "test-01": {
            "backups": false,
            "created_at": "2020-03-18T04:10:53Z",
            "disk": 50,
            "id": "",
            "image": "ubuntu-18-04-x64",
            "ipv4_address": "192.245.252.9",
            "ipv4_address_private": "10.136.185.151",
            "ipv6": false,
            "ipv6_address": "",
            "ipv6_address_private": null,
            "locked": false,
            "memory": 2048,
            "monitoring": false,
            "name": "test-01",
            "price_hourly": 0.01488,
            "price_monthly": 10,
            "private_networking": true,
            "region": "nyc1",
            "resize_disk": true,
            "size": "s-1vcpu-2gb",
            "ssh_keys": [""],
            "status": "active",
            "tags": ["test"],
            "urn": "do:droplet:185238864",
            "user_data": null,
            "vcpus": 1,
            "volume_ids": [],
            "ansible_host": "192.245.252.9",
            "ansible_user": "root"
          }
        },
        "vars": {
          "projects": {
            "TerraformCloud": {
              "created_at": "2020-03-18T04:04:29Z",
              "description": "Terraform Cloud Project",
              "environment": "Development",
              "id": "",
              "name": "TerraformCloud",
              "owner_id": ,
              "owner_uuid": "",
              "purpose": "Terraform Cloud Project",
              "resources": ["do:droplet:185238864"],
              "updated_at": "2020-03-18T04:04:29Z"
            }
          }
        }
      },
      "test": {
        "hosts": {
          "test-01": {}
        },
        "vars": {},
        "children": {}
      }
    }
  }
}
```
