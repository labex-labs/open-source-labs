#!/bin/zsh
cd ~/project
git init
git config --global user.email 'labex@labex.io'
git config --global user.name 'LabEx'
git add .
git commit -m 'init'

pip install matplotlib
cd ~/project
/usr/local/bin/pip install jupyter >/dev/null 2>&1
mkdir ~/.jupyter
cat >>~/.jupyter/jupyter_notebook_config.py <<EOF
# Configuration file for notebook.
c = get_config()
c.ExtensionApp.default_url = '/tree/custom-figure-class.ipynb.ipynb'
c.LabServerApp.open_browser = False
c.ServerApp.disable_check_xsrf = True
c.ServerApp.allow_root = True
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.password = ''
c.ServerApp.password_required = False
c.ServerApp.port = 8080
c.ServerApp.root_dir = '/home/labex/project'
c.ServerApp.token = ''
c.ServerApp.tornado_settings = {"headers": {"Content-Security-Policy": "frame-ancestors self https://labex.io"}}
EOF

chmod 644 ~/.jupyter/jupyter_notebook_config.py
export PATH=$PATH:/home/labex/.local/bin

nohup /home/labex/.local/bin/jupyter notebook >/dev/null 2>&1 &

# Wait for notebook service
sleep 1
