# Configuration file for Jupyter Hub
c = get_config()

# Base configuration
c.JupyterHub.ip = "0.0.0.0"
c.JupyterHub.port = 80
c.JupyterHub.log_level = 10
c.JupyterHub.pid_file = "{{ root }}/pid"
c.JupyterHub.confirm_no_ssl = True
c.Authenticator.admin_users = admin = set()

# Set the full path to the singleuser server
c.LocalProcessSpawner.cmd = ["/usr/local/bin/jupyterhub-singleuser"]

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
