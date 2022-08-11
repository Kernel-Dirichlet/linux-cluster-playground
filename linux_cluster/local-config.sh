echo "Configuring Linux cluster..."
sudo docker network create --driver bridge linux_swarm
sudo docker compose --file user_config.yml up -d
echo "Linux cluster configured!"

