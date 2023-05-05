# Create Function with Parameters

## Problem

Create a Bash script named `function_parameter.sh`, containing a function called `Rectangle_Area`. The function should calculate the area of a rectangle based on two passed-in parameters, which will be represented as $1 and $2 within the function itself. After defining the function, call it with two sample parameters (e.g. 10 and 20).

## Requirements

To successfully complete this challenge, the script should:

* Declare a function named `Rectangle_Area`
* Read in two parameters (e.g. width and height)
* Calculate the area of a rectangle based on the provided parameters
* Print the result
* Call the `Rectangle_Area` function with two sample parameters (e.g. 10 and 20)

## Solution

The following code can be used to create the `function_parameter.sh` script.

```bash
#!/bin/bash

Rectangle_Area() {
    area=$(($1 * $2))
    echo "Area is : $area"
}

Rectangle_Area 10 20
```

To run the script, execute the following command in the terminal:
```bash
$ bash function_parameter.sh
```

This will produce the output:
```bash
Area is : 200
```
This means that the `Rectangle_Area` function has correctly calculated the area of a rectangle with width 10 and height 20, and printed the result.
