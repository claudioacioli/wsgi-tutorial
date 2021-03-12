# StartProject
```bash
# Create lxc container
lxc-create -t ubuntu -n wsgi

# Start container
lxc-start wsgi

# Figure out the ip of new container
lxc-ls --fancy

# Connect with container
ssh ubuntu@192.168...

# update and upgrade and install some packages
sudo apt update
sudo apt upgrade -y
sudo apt install -y git curl ca-certificates

# Set git globals
git config --global user.email "your@email.com"
git config --global user.name "YourName"

# install python venv packaage
sudo apt install python3-venv

# Pull repository
git clone https://github.com/claudioacioli/wsgi-tutorial.git wsgi

# Go to repository
cd wsgi

# Create a virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bind/activate

# Run it
python env.py

# Test it
curl 127.0.0.1:8080
```

