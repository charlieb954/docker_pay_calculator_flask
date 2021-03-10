# stop all running containers
#sudo docker stop $(sudo docker ps -a -q)

# remove all exited containers
#sudo docker rm -f $(sudo docker ps -a -q)

# bring down the containers
sudo docker-compose down

# removing hanging containers
sudo docker system prune
