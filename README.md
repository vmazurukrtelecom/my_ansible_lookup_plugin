# My Ansible Lookup Plugin

Custom Ansible lookup plugin for AWX, providing dynamic lookup functionality for inventory variables.

created for test puroses with the help of grok3

Usage
This plugin (my_custom_cred_lookup) writes the inventory_hostname and current timestamp to /tmp/lookup.txt

## Installation

Install the plugin using pip:

```bash
awx-python -m pip install git+https://github.com/vmazurukrtelecom/my_ansible_lookup_plugin.git
```
