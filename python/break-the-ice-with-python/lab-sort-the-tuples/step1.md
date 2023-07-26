# Sort the Tuples

You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

- **_1: Sort based on name_**
- **_2: Then sort based on age_**
- **_3: Then sort by score_**

The priority is that name > age > score.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/sort_the_tuples.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def sort_the_tuples():
    lst = []
    while True:
        s = input().split(',')
        if not s[0]:                          # breaks for blank input
            break
        lst.append(tuple(s))

    # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
    lst.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
    print(lst)


sort_the_tuples()

```

This Python code defines a function called `sort_the_tuples()` that sorts a list of tuples based on the values of their elements. The function prompts the user to input a series of comma-separated values that will be used to create tuples. The input process continues until the user enters a blank input.

The function creates an empty list called `lst` to store the tuples. It then uses a `while` loop to continuously prompt the user for input and append the input values as a tuple to the `lst` list. The `while` loop continues until the user enters a blank input.

The function then uses the `sort()` method to sort the tuples in the `lst` list based on the values of their elements. The `key` parameter is used to define a sorting key that specifies the order in which the elements should be sorted. In this case, the sorting key is defined using a lambda function that sorts the tuples by the values of their elements in ascending order of priority: first by the value of the first element, then by the value of the second element (converted to an integer), and finally by the value of the third element (also converted to an integer).

Finally, the function uses the `print()` function to output the sorted `lst` list to the console.

Overall, this code demonstrates how to use a `while` loop, the `sort()` method, and a lambda function to sort a list of tuples based on the values of their elements in Python.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/sort_the_tuples.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
```

Then, the output of the program should be:

```bash
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
```

At this point, your code is running successfully!
