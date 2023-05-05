## Solution

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

