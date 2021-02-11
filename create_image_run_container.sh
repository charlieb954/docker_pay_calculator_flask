sudo docker build -t website_build .
sudo docker run -d -p 80:8080 website_build
sudo docker ps -a
echo 'running on port 80 at:'
hostname -I | awk '{print $1}'

