# Ansible

## Dependencies
```sh
ansible-galaxy install AnsibleShipyard.ansible-zookeeper
```

## Ansible Environment
`http://docs.ansible.com/ansible/intro_installation.html`
this code to make sure you set it up correctly:
```sh
ansible --version
```

Ansible metadata`/etc/ansible`:
```sh
sudo chmod -R 777 /etc/ansible
```

Ansible Dynamic Inventory Download these to `/etc/ansible`:
* https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.ini
* https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py

Run this to grant permission:
```sh
chmod +x /etc/ansible/ec2.py
```

Change Ansible config `/etc/ansible/ansible.cfg`:
```ini
inventory = /etc/ansible/ec2.py
host_key_checking = False
```
