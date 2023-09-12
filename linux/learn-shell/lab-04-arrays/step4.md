# Determine the number of names

To determine the number of names in the `NAMES` array, we can use the special variable `$#`. Add the following code to assign the length of the `NAMES` array to the `NumberOfNames` variable:

```shell
NumberOfNames=${#NAMES[@]}
```
