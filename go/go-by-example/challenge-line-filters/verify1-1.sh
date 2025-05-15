#!/bin/bash
# To try out our line filter, first make a file with a few
# lowercase lines.
cd /home/labex/project
echo 'hello' > /tmp/lines
cd /home/labex/project
echo 'filter' >> /tmp/lines

# Then use the line filter to get uppercase lines.
cd /home/labex/project
cat /tmp/lines | /usr/local/go/bin/go run line-filters.go | grep "HELLO"
