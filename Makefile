PORT = 5001
IP_ADDR = localhost

# run the containers in detatched mode and force rebuild
docker-run:
	sudo docker-compose up -d --build
	echo 'Flask application running on ${IP_ADDR}:${PORT}'

# stop all running containers
docker-stop-all:
	sudo docker stop $(sudo docker ps -a -q)

# remove all exited containers
docker-remove-all:
	sudo docker rm -f $(sudo docker ps -a -q)

docker-stop:
	sudo docker-compose down

# removing hanging containers
docker-prune:
	sudo docker system prune
