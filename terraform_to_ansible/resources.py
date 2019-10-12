""" Definitions of all resources available."""

# Define the different supported resource_types
RESOURCE_TYPES = ['azurerm_public_ips',
                  'azurerm_subnets', 'azurerm_virtual_machines',
                  'azurerm_network_interfaces', 'azurerm_network_interfaces']


def resource_types():
    """Define all resources as dictionary."""
    types = dict()
    for resource in set(RESOURCE_TYPES):
        types[resource] = list()

    return types
