#!/bin/bash

cd ~/project/data-types && echo 1 | cargo run | grep -q "2"
