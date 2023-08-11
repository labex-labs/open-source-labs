# Multi-line Comment

Create a Bash script that calculates the area of a rectangle. The script should prompt the user to enter the length and width of the rectangle, and then calculate and display the area. Use multi-line comments to explain the purpose of the script and any important details.

- The script should be named `rectangle-area.sh`.
- The script should prompt the user to enter the length and width of the rectangle.
- The script should calculate the area of the rectangle using the formula `area = length * width`.
- The script should display the calculated area to the user.
- Use multi-line comments to explain the purpose of the script and any important details.

Create a new Bash script named `rectangle-area.sh` and add the following code:

```bash
#!/bin/bash
: '
This script calculates the area of a rectangle.
The user will be prompted to enter the length and width of the rectangle.
The area will be calculated using the formula area = length * width.
The calculated area will be displayed to the user.
'
echo "Enter the length of the rectangle: "
read length
echo "Enter the width of the rectangle: "
read width
area=$((length * width))
echo "The area of the rectangle is: $area"
```

Save the file and make it executable using the command `chmod +x rectangle-area.sh`. Then, run the script using the command `./rectangle-area.sh`.
