#!/bin/zsh

# Download the setup script and run it
wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh

# Create the initial follow.py file
cat > /home/labex/project/follow.py << 'EOF'
import os
import time

def follow(filename):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)    # Sleep briefly to avoid busy wait
                continue
            yield line
EOF

# Create the initial cofollow.py file
cat > /home/labex/project/cofollow.py << 'EOF'
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def printer():
    while True:
        item = yield
        print(item)
EOF

# Create a sample log file for testing
cat > /home/labex/project/stocklog.csv << 'EOF'
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
"AA",39.58,"6/11/2007","09:39.28",-0.08,39.67,39.58,39.31,243159
"HPQ",45.94,"6/11/2007","09:39.29",0.24,45.80,45.94,45.59,408919
"IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
EOF
