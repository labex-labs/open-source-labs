#!/bin/zsh

# cd /tmp                                                                                                           
# python3 *_test.py

check_results=`python3 /home/labex/project/compress_and_decompress_the_string.py`
if [[ $check_results =~ "b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
b'hello world!hello world!hello world!hello world!'" ]] 
then 
    echo true
else 
    echo false
fi

