#!/usr/bin/env bash
# Script for setting up web servers for web_static deployment

# Install Nginx if not installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders if they don't exist
folders=("/data" "/data/web_static" "/data/web_static/releases" "/data/web_static/shared" "/data/web_static/releases/test")
for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ]; then
        sudo mkdir -p "$folder"
    fi
done

# Change ownership specifically for /data
sudo chown -R ubuntu:ubuntu "/data"

# Create fake HTML file for testing
html_content="<html>
<head>
    <title>Test Page</title>
</head>
<body>
    Testing Nginx configuration
</body>
</html>"
html_path="/data/web_static/releases/test/index.html"
echo "$html_content" | sudo tee "$html_path" > /dev/null

# Create or recreate symbolic link
symbolic_link="/data/web_static/current"
if [ -L "$symbolic_link" ]; then
    sudo rm "$symbolic_link"
fi
sudo ln -s /data/web_static/releases/test/ "$symbolic_link"

# Update Nginx configuration
nginx_config="/etc/nginx/sites-enabled/default"
sudo sed -i '/hbnb_static/ d' "$nginx_config"
nginx_content="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/server_name _;/a $nginx_content" "$nginx_config"

# Restart Nginx
sudo service nginx restart
