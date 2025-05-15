#!/bin/bash
# Use these commands to run the example.
# (Note: due to limitation on go playground,
# this example can only be run on your local machine.)
cd /home/labex/project
mkdir -p folder
cd /home/labex/project
echo "hello go" > folder/single_file.txt
cd /home/labex/project
echo "123" > folder/file1.hash
cd /home/labex/project
echo "456" > folder/file2.hash

cd /home/labex/project
/usr/local/go/bin/go run embed-directive.go | grep "hello go"
