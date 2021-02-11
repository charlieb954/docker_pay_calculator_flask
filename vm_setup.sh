sudo apt update
sudo apt install vim -y
sudo apt install git -y

#update your existing list of packages:
sudo apt update

#install a few prerequisite packages which let apt use packages over HTTPS:
sudo apt install apt-transport-https ca-certificates curl software-properties-common

#add the GPG key for the official Docker repository to your system:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add the Docker repository to APT sources:
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

# update packages
sudo apt update

# Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:
apt-cache policy docker-ce

# finally install docker
sudo apt install docker-ce -y

# check the daemon is running
sudo systemctl status docker

sudo apt install net-tools
