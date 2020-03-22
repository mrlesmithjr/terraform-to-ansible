commit f22a6cb2f9b277f0726c69d713688e3ae8d105cb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 17:05:40 2020 -0400

    Updated after tweaking cookiecutter template

commit 6a576273d6b52873afa7d7354428b3d062440014
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 15:38:33 2020 -0400

    Updated: changelog

commit a11312fdafbad68d7d9a61ac4ec02fba85b75816
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 15:38:22 2020 -0400

    Disabled Python 3.5 and 3.6 testing

commit dadee33d66c7b8b9895cbf5cea9689305b399a6f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 15:38:04 2020 -0400

    Added missing YAML requirement

commit 69ea42b9a74f18e5470bcbd12cb671deb5280069
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 15:37:49 2020 -0400

    Disabled Python 3.5 and 3.6 testing

commit f7a3249aa86912712f4a7f205e8769d610e85974
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 15:24:53 2020 -0400

    New files, etc. from cookiecutter template

commit 7d31d39e5b5680ae18ed0bbd7960c37045638519
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 15:22:30 2020 -0400

    Deleted old tests, etc. not needed
    
    These files are no longer required for new format

commit f1af518e5c8cbc97e22cea15ba2a5b462533ed19
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 15:21:38 2020 -0400

    Updated files, etc. after new structure
    
    This aligns to cookiecutter template

commit 66ea87e1934cc135872c64406a920c4283e518b9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 15:10:55 2020 -0400

    Fixed linting issues

commit c31e94488337180b46ff3091e733bb213ee4bad8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 15:10:41 2020 -0400

    Added info on vSphere support

commit 4a2711a6517a27d96801d36c3c1d481fe4f87098
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 13:39:02 2020 -0400

    Added initial vSphere support
    
    Still needs some work but it works as generating a usable Ansible inventory
    I've tested successfully in its current state

commit 9e6c3a81f45d4664deafd8eb7e3e6dc5bedeb056
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 13:37:29 2020 -0400

    Added ansible.cfg for quick testing of Ansible
    
    This will ensure that SSH keys are ignored, etc.

commit 05dcef99dbed2631807eec5d80c2c3be8813efc0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 02:13:03 2020 -0400

    Added: Loading options and usage guide
    
    Can now load from file or directory
    
    Added initial usage guide

commit fa201a110caa2cb7a1f7560f70bd7a937a4b9c01
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 17 14:37:51 2020 -0400

    Added --ansibleHost argument
    
    By default --ansibleHost is 'public'.
    If you use --ansibleHost private, ansible_host will use private address

commit 0ef71393b39c5b65ebe4ce5091a778d659622683
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 16 22:27:40 2020 -0400

    Added: Firewalls, projects and ssh keys
    
    We add these to vars for now. May use them in another way later.

commit f05be8f4fcd07b84c3a269b629cd1e34f67b999a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 16 22:26:54 2020 -0400

    Removed modules as this was from older versions
    
    Not backporting prior versions at this time

commit bca1cf9a02d3780257f10a10292ff418db7c98b9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 16 22:26:17 2020 -0400

    Added: Capture of Terraform version
    
    This will capture the version of Terraform used.
    This will be used at some point to determine logic if needed based on version

commit 22cc2a664f7fc4ff7dc466e4a4d6464946956969
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 15 00:21:50 2020 -0400

    Added: DigitalOcean DNS records

commit 32b6f2f8bec9641059541583b894db52fe21e954
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 14 22:28:46 2020 -0400

    Updated: Python requirements

commit e0e02a90ed1d2d0b00cc4a2575df494d891fc40a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 14 22:21:56 2020 -0400

    Updated: changelog

commit d3b48b0c0badc6cda136f9fc2d3fd18e0b1ba655
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 14 22:21:43 2020 -0400

    Added logging for resource mapping failures

commit fb1bb010c13b5aef00a65939bab39d81be006ab4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 14 01:24:47 2020 -0400

    Added: DigitalOcean domain type

commit bb19b32aa38b3e9c42a4b8ff03895e7a199972e8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 14 01:24:15 2020 -0400

    Added: Logging for resource_type and DO resource_config

commit f35b829478a964e69af25eaa2d562a55ca878ed5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 13 20:13:35 2020 -0400

    Cleanup, new features, etc.
    
    Lot's of work needed to get this more consumable. Will be rewriting
    portions that already existed for AzureRM. New stuff for DigitalOcean
    added.

commit c03cac7bb6958bc91c802be7c881804815a1cb94
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 13 20:12:50 2020 -0400

    Added: Beginning of DigitalOcean support

commit 94b44280221557d23ef711a0eccea0d694803d8c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 13 20:11:18 2020 -0400

    Added: First logging setup
    
    Needs some work still

commit 1f5617f9a6615ba1d675d2dc485b23b698b6aa28
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 13 20:09:04 2020 -0400

    Renamed args to cli

commit b1a33681ecbd288a2d8bb9d129a67356dbf6f7a1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Oct 14 14:37:32 2019 -0400

    First commit of basic Ansible inventory
    
    - This is the first commit of basic Ansible inventory generation for
    Azure virtual machines only.
    - Functionality will increase based on additional requirements and
    samples.

commit 92fd9e72a8fe01a78c6dea59653d26144d5331d6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Oct 14 14:36:46 2019 -0400

    Updated Python development requirements

commit 548b0109390df1a873f3f58cc3a943b34e5c972a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Oct 13 00:38:57 2019 -0400

    Simplified parsers
    
    - We now dynamically parse resources so the original modules are no
    longer needed or required.

commit 4accce8fa6db599e9e751dad9dfc786e3adf481f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 11 21:16:55 2019 -0400

    Simplified types dict generation
    
    - No need to use f'{resource}'

commit 2babaf3f3d97d52992e87cdd8e7dfdd22fbd4b18
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 11 21:14:18 2019 -0400

    Changed resource types to use a list
    
    - This will allow for additional resource types to be added much easier
    - Assumption is that all resource types will be a list

commit 77009a1dd5fb24dd4b2a6bb9e20b0597acf8dc41
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 11 21:13:15 2019 -0400

    Commented out arg validations
    
    - These were lingering from commenting out the previous args

commit 625e7984b523dc7658dac59ee57d96d553c11b21
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 10 22:22:58 2019 -0400

    Updated current available arguments
    
    - Commented out currently unavailable CLI arguments. There were some
    that were available but not implemented yet.

commit 5ae741193bd5100374f46203fd4af27c73edafaa
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 10 22:08:06 2019 -0400

    First commit of Azure RM NICs
    
    - Added initial parsing of Azure RM network interfaces
    - When we add the generation of Ansible inventory we will convert these
    to a dictionary based on the id to allow for easy lookups for VMs

commit 181a2df0fed3666bdfac9e4c7e1821dba56d12fd
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 10 21:37:29 2019 -0400

    Added initial Azure RM VM parsing
    
    - This is the initial parsing for Azure RM VMs.

commit 5f656c55295cf2d47217e330bb23ea4c45f85640
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 10 17:08:13 2019 -0400

    Added GitHub Actions Workflow
    
    - First commit of GitHub Actions Workflow
    - This will grow over time

commit fbd8bebcc230b9150f86664752c8cba18a6cb1f5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 10 17:05:26 2019 -0400

    Removed .vscode directory
    
    - This should not be included

commit 3ab1cebb83d8f6dd403315d229ddf61f92017401
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 10 17:02:03 2019 -0400

    First commit
    
    - Initial parsing of Azure RM public IPs
    - Initial parsing of Azure RM subnets
    - Generating Ansible inventory is not yet implemented
