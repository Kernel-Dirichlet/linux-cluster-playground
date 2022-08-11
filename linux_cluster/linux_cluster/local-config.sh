echo "Configuring Linux cluster..."
sudo docker network create --driver bridge linux_swarm
sudo docker compose --file linux_cluster-compose.yml up -d
echo "Linux cluster configured!"

