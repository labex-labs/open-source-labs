#!/bin/zsh

# Create necessary files for the lab
touch /home/labex/project/stocklog.csv
mkdir -p /home/labex/project

# Download the required modules and helper files
wget -q -O /home/labex/project/structure.py https://raw.githubusercontent.com/dabeaz-course/practical-python/master/Notes/08_Testing_debugging/02_Logging/structure.py
wget -q -O /home/labex/project/tableformat.py https://raw.githubusercontent.com/dabeaz-course/practical-python/master/Notes/07_Advanced_Topics/03_Returning_functions/tableformat.py

# Generate some sample data for the stocklog.csv file
cat > /home/labex/project/stocklog.csv << 'EOF'
GOOG,100.02,6/11/2007,09:30:01,0.01,100.01,100.05,99.95,75000
AAPL,102.5,6/11/2007,09:30:02,0.02,102.48,102.55,102.45,60000
IBM,50.1,6/11/2007,09:30:03,-0.15,50.25,50.3,50.1,85000
MSFT,72.5,6/11/2007,09:30:04,-0.25,72.75,72.8,72.5,65000
CAT,64.8,6/11/2007,09:30:05,0.05,64.75,64.9,64.7,45000
AA,35.25,6/11/2007,09:30:06,-0.15,35.4,35.45,35.2,92000
EOF

# Set up a simple "stocksim.py" that will append to the stocklog file periodically
cat > /home/labex/project/stocksim.py << 'EOF'
import time
import random
import csv
import os

def generate_stock_data():
    stocks = [
        {"name": "GOOG", "price": 100.02},
        {"name": "AAPL", "price": 102.5},
        {"name": "IBM", "price": 50.1},
        {"name": "MSFT", "price": 72.5},
        {"name": "CAT", "price": 64.8},
        {"name": "AA", "price": 35.25}
    ]
    
    while True:
        for stock in stocks:
            change = round(random.uniform(-0.5, 0.5), 2)
            stock["price"] = round(stock["price"] + change, 2)
            
            # Get current date and time
            date = time.strftime("%m/%d/%Y")
            current_time = time.strftime("%H:%M:%S")
            
            # Calculate other fields
            open_price = round(stock["price"] - change, 2)
            high_price = round(max(stock["price"], open_price) + random.uniform(0, 0.1), 2)
            low_price = round(min(stock["price"], open_price) - random.uniform(0, 0.1), 2)
            volume = random.randint(10000, 100000)
            
            # Write to CSV
            with open("stocklog.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([
                    stock["name"],
                    stock["price"],
                    date,
                    current_time,
                    change,
                    open_price,
                    high_price,
                    low_price,
                    volume
                ])
        
        time.sleep(2)  # Update every 2 seconds

# Start the stock simulator in background
if __name__ == "__main__":
    print("Stock simulator running. Press Ctrl+C to stop.")
    generate_stock_data()
EOF

# Start the stock simulator in the background
python3 /home/labex/project/stocksim.py > /dev/null 2>&1 &

# Set up shell history
wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh
