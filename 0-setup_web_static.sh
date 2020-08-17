#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

#Installs nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the folder it doesn’t already exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html
# (with simple content, to test the Nginx configuration)
echo "Holberton test" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the 
# /data/web_static/releases/test/ folder. If the symbolic link already exists
# it is deleted and recreated every time the script is ran.
rm -fr /data/web_static/current
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group recursively
sudo chown -R ubuntu:ubuntu /data/

# Updates the Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static (ex: https://mydomainname.tech/hbnb_static).
new_lines='server_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}\n'
search='server_name _;'
sudo sed -i "s/$search/$new_lines/" /etc/nginx/sites-available/default

# Restarts Nginx after updating the configuration
sudo service nginx restart
