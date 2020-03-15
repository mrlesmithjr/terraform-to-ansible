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
