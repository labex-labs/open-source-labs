# The Intersection of Two Lists

With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/intersection_of_two_lists.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def intersection_of_two_lists():
    list1 = [1, 3, 6, 78, 35, 55]
    list2 = [12, 24, 35, 24, 88, 120, 155]
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    print(intersection)


intersection_of_two_lists()

```

This Python code defines a function called `intersection_of_two_lists`. Within the function, two lists `list1` and `list2` are defined.

The `set` function is then used to convert `list1` and `list2` into sets `set1` and `set2`, respectively.

The `&` operator is used to find the intersection of `set1` and `set2`, which is stored in the variable `intersection`.

Finally, the resulting intersection set is printed to the console using the `print` function.

Overall, this code demonstrates how to use sets in Python to find the intersection of two lists.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/intersection_of_two_lists.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
{35}
```

At this point, your code is running successfully!
