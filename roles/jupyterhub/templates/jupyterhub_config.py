# Configuration file for Jupyter Hub
c = get_config()

import os
import sys

# Base configuration
c.JupyterHubApp.ip = "0.0.0.0"
c.JupyterHubApp.log_level = 10
c.JupyterHubApp.pid_file = "{{ root }}/pid"
c.JupyterHubApp.admin_users = admin = set()

# Set the full path to the singleuser server
c.LocalProcessSpawner.cmd = ["{{ venv }}/bin/jupyterhub-singleuser"]

# Configure the authenticator
c.Authenticator.whitelist = whitelist = set()

# Add users to the admin list, the whitelist, and also record their user ids
with open("{{ root }}/userlist") as f:
    for line in f:
        if not line:
            continue
        parts = line.split()
        name, userid = parts[0].split(":")
        whitelist.add(name)
        if len(parts) > 1 and parts[1] == 'admin':
            admin.add(name)

