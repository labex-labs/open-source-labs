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
