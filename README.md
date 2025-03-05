# My Ansible Lookup Plugin

Custom Ansible lookup plugin for AWX, providing dynamic lookup functionality for inventory variables.

created for test puroses with the help of grok3


REF: https://grok.com/share/bGVnYWN5_d4ee8768-6989-4881-8815-2026a4a5c5be


Usage
This plugin (my_custom_cred_lookup) writes the inventory_hostname and current timestamp to /tmp/lookup.txt

## Installation

Install the plugin using pip:

```bash
awx-python -m pip install git+https://github.com/vmazurukrtelecom/my_ansible_lookup_plugin.git
```
