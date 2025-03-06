#!/bin/zsh
cd ~/project
git init
git config --global user.email 'labex@labex.io'
git config --global user.name 'LabEx'
git add .
git commit -m 'init'

pip install matplotlib
cd ~/project
pip install jupyter
mkdir ~/.jupyter
cat >> ~/.jupyter/jupyter_notebook_config.py << EOF
# Configuration file for notebook.
c = get_config()
c.ExtensionApp.default_url = '/tree/set-alpha.ipynb'
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

mkdir ~/.jupyter/custom/
cat >> ~/.jupyter/custom/custom.css << EOF
div#top-panel-wrapper {
  display: none !important;
}

#menu-panel-wrapper {
  display: none !important;
}

.lm-Widget.jp-CommandToolbarButton.jp-nb-interface-switcher-button.jp-Toolbar-item {
  display: none !important;
}

div#main-panel {
  top: unset !important;
  height: inherit !important;
}

div#id-14077fc4-ca32-414c-96b0-d75db622097f {
  height: inherit !important;
}
EOF

chmod 644 ~/.jupyter/jupyter_notebook_config.py
export PATH=$PATH:/home/labex/.local/bin

nohup /home/labex/.local/bin/jupyter-notebook > /dev/null 2>&1 &

# Create the jupyter notebook file
cat > ~/project/set-alpha.ipynb << EOF
{
 "cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
EOF

# Wait for notebook service
sleep 1
