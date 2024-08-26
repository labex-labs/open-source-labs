cd ~/project

curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

sudo apt-get update
sudo apt-get install -y nodejs

unzip demo.zip && mv demo/* ./ && rm -rf demo*
