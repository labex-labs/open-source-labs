#!/bin/bash
# Ensure text-templates.go is present, or rename templates.go if it exists
if [ -f templates.go ] && [ ! -f text-templates.go ]; then
  mv templates.go text-templates.go
elif [ ! -f text-templates.go ]; then
  # If neither exists, create a placeholder or ensure the lab provides it
  echo "// Placeholder for text-templates.go" > text-templates.go
fi
