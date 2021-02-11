# stop all running containers
sudo docker stop $(sudo docker ps -a -q)

# remove all exited containers
sudo docker rm -f $(sudo docker ps -a -q)

# removing hanging containers
sudo docker system prune
