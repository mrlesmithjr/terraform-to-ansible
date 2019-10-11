""" Definitions of all resources available."""


def resource_types():
    """Define all resources as dictionary."""
    types = dict()
    types['azurerm_public_ips'] = list()
    types['azurerm_subnets'] = list()
    types['azurerm_virtual_machines'] = list()
    types['azurerm_network_interfaces'] = list()

    return types
