#!/bin/bash
if grep -q "unique_routes" ~/.python_history && grep -q "total_rides_by_route" ~/.python_history && grep -q "rides_2001" ~/.python_history && grep -q "rides_2011" ~/.python_history; then
  exit 0
else
  exit 1
fi
