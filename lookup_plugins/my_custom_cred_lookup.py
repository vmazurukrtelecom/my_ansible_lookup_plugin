from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
from datetime import datetime

class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        # Отримуємо inventory_hostname із змінних Ansible
        inventory_hostname = variables.get('inventory_hostname')

        if not inventory_hostname:
            raise AnsibleError("inventory_hostname is not defined")

        # Отримуємо поточний час у форматі "YYYY-MM-DD HH:MM:SS"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Записуємо inventory_hostname і поточний час у файл /tmp/lookup.txt
        try:
            with open('/tmp/lookup.txt', 'a') as f:
                f.write(f"{current_time} - {inventory_hostname}\n")
        except IOError as e:
            raise AnsibleError(f"Failed to write to /tmp/lookup.txt: {str(e)}")

        # Повертаємо значення inventory_hostname
        return [inventory_hostname]
