# Print an Alphabet Rangoli

You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

## Example

Different sizes of alphabet rangoli are shown below:

```bash
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

## Preparation

Before we start writing the code, we should open the `/home/labex/project/print_an_alphabet_rangoli.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def rangoli(n):
    l1 = list(map(chr, range(97, 123)))
    x = l1[n-1::-1]+l1[1:n]
    mid = len('-'.join(x))
    for i in range(1, n):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid, '-'))
    for i in range(n, 0, -1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid, '-'))


rangoli(5)

```

This Python code defines a function called `rangoli` that takes an integer `n` as input. The function generates a rangoli pattern of size `n`.

Within the function, a list `l1` is created using the `map` function and the `range` function. The `map` function is used to convert the integer values to their corresponding ASCII characters, and the `range` function is used to generate a range of integers from 97 to 122, which correspond to the ASCII values of lowercase letters a to z.

The variable `x` is then created by concatenating a slice of `l1` that goes from the `n-1`th element to the beginning of the list in reverse order, with a slice of `l1` that goes from the 1st element to the `n`th element.

The variable `mid` is then calculated as the length of the string obtained by joining the elements of `x` with the `-` character.

Two `for` loops are then used to generate the top and bottom halves of the rangoli pattern. The first `for` loop iterates from 1 to `n-1`, and the second `for` loop iterates from `n` to 1.

Within each `for` loop, the `join` function is used to concatenate a slice of `l1` that goes from the `n-1`th element to the `n-i`th element in reverse order, with a slice of `l1` that goes from the `n-i`th element to the `n`th element. The resulting string is then centered using the `center` method with the `mid` value and the `-` character as the fill character.

Finally, the resulting rangoli pattern is printed to the console using the `print` function.

Overall, this code demonstrates how to use string manipulation and loops in Python to generate a rangoli pattern of a given size.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/print_an_alphabet_rangoli.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

At this point, your code is running successfully!
