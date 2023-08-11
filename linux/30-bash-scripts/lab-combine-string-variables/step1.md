# Combine String Variables

Create a Bash script that demonstrates how to combine string variables. The script should define two string variables, concatenate them using the `+` operator, and append a string to the concatenated result.

- The script should be named `string_combine.sh`.
- The script should define two string variables named `string1` and `string2`.
- The script should concatenate `string1` and `string2` using the `+` operator and store the result in a variable named `string3`.
- The script should append the string " is a good tutorial blog site" to `string3`.
- The script should output the value of `string3`.

```bash
#!/bin/bash

string1="Linux"
string2="Hint"
string3="$string1$string2"
string3+=" is a good tutorial blog site"
echo $string3
```
