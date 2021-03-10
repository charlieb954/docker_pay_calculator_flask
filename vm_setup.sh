# Get updates and install vim and git.
sudo apt update
sudo apt install vim -y
sudo apt install git -y

# Update your existing list of packages:
sudo apt update

# Install a few prerequisite packages which let apt use packages over HTTPS:
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Add the GPG key for the official Docker repository to your system:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add the Docker repository to APT sources:
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

# Update packages
sudo apt update

# Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:
apt-cache policy docker-ce

# Finally install docker
sudo apt install docker-ce -y

# Check the daemon is running
sudo systemctl status docker

sudo apt install net-tools

# Add current user to docker group to avoid using "sudo" for every command
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
