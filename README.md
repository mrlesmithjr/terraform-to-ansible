---
title: terraform_to_ansible
---

Consume Terraform tfstate and generate usable Ansible inventory.

## Build Status

### GitHub Actions

![Python Test](https://github.com/mrlesmithjr/python-terraform-to-ansible/workflows/Python%20Test/badge.svg)

### Travis CI

[![Build Status](https://travis-ci.org/mrlesmithjr/python-terraform-to-ansible.svg?branch=master)](https://travis-ci.org/mrlesmithjr/python-terraform-to-ansible)

## Requirements

- [requirements.txt](requirements.txt)
- [requirements-dev.txt](requirements-dev.txt)

## Backends Support

- Local
- Terraform Cloud

## Providers Supported

The following providers are currently supported:

- AzureRM (Minimal or disable due to refactoring)
- DigitialOcean
- VMware vSphere (Tested with Terraform `0.11.14`)

## Usage

To view the different usages available checkout the [usage](USAGE.md) guide.

## Dependencies

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://twitter.com/mrlesmithjr)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
- [http://everythingshouldbevirtual.com](http://everythingshouldbevirtual.com)

> NOTE: Repo has been created/updated using [https://github.com/mrlesmithjr/cookiecutter-python-project](https://github.com/mrlesmithjr/cookiecutter-python-project) as a template.
