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

## The GPU role

Note that if you want to run the GPU role, which installs CUDA and cuDNN, you
will need to manually download the CUDA and cuDNN files and place them in the
`roles/gpu/files` directory. The files you need are:

* cuda-repo-ubuntu1604_8.0.44-1_amd64.deb (can be downloaded from https://developer.nvidia.com/cuda-downloads )
* cudnn-8.0-linux-x64-v5.0-ga.tgz (can be downloaded from https://developer.nvidia.com/cudnn )

## Running the playbook

Run it with:

    ansible-playbook site.yml -i inventory
