# run the containers in detatched mode
sudo docker-compose up -d
echo 'running application on port 80 at:'
hostname -I | awk '{print $1}'