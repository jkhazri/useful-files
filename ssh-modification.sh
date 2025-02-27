#!/bin/bash

# Define variables
SSH_KEYS_URL="https://raw.githubusercontent.com/jkhazri/useful-files/refs/heads/main/ssh-keys.txt"
SSHD_CONFIG_URL="https://raw.githubusercontent.com/jkhazri/useful-files/refs/heads/main/sshd-config"
AUTHORIZED_KEYS_PATH="/home/onecloud/.ssh/authorized_keys"
SSHD_CONFIG_PATH="/etc/ssh/sshd_config"

# Ensure the .ssh directory exists
mkdir -p /home/onecloud/.ssh

# Download the SSH keys and set proper permissions
curl -sL "$SSH_KEYS_URL" -o "$AUTHORIZED_KEYS_PATH"
chown onecloud:onecloud "$AUTHORIZED_KEYS_PATH"
chmod 600 "$AUTHORIZED_KEYS_PATH"

# Download the SSH daemon configuration
curl -sL "$SSHD_CONFIG_URL" -o "$SSHD_CONFIG_PATH"

# Restart the SSH service
systemctl restart sshd

echo "SSH keys and configuration updated. SSH service restarted."
