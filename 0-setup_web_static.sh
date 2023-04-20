#!/usr/bin/env bash
#A bash script that sets up web servers

sudo apt-get update
sudo apt-get install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared /data/web_static/current
sudo touch /data/web_static/releases/test/index.html
echo "Testing the configurations" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo service nginx restart


