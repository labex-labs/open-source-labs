#!/bin/zsh
docker info --format '{{json .ContainersRunning}}' | grep "0"