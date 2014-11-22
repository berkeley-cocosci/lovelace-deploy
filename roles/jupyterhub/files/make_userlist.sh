#!/bin/bash

# remove existing file
rm -f $1

# populate jupyterhub users
users=$(cut -d: -f1 /etc/passwd)
for user in $users; do
    is_jupyterhub_admin=$(groups $user | grep "\\bjupyterhub_admins\\b")
    if [[ ! -z "$is_jupyterhub_admin" ]]; then
        echo "$user:$(id -u $user) admin" >> $1
    fi

    is_jupyterhub_user=$(groups $user | grep "\\bjupyterhub_users\\b")
    if [[ ! -z "$is_jupyterhub_user" ]]; then
        echo "$user:$(id -u $user)" >> $1
    fi
done
