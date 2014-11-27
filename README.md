# Lovelace deployment

This repository contains an Ansible playbook for configuring the lovelace server
for the cocosci lab. It configures the following things:

* Julia
* Python
* R
* JupyterHub

## Adding a new user

1. `sudo adduser <username>`
2. `sudo adduser <username> jupyterhub_users` or `sudo adduser <username> jupyterhub_admins`
3. If JupyterHub is currently running, add their username through the admin
   interface.
4. Add them to the server mailing list.

## Running the playbook

Run it with:

    ansible-playbook site.yml -i inventory
