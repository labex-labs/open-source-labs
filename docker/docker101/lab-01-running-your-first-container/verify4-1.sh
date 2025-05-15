#!/bin/bash
docker info --format '{{json .ContainersRunning}}' | grep "0"
