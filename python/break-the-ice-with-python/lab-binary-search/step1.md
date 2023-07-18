# Binary Search

Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/binary_search.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = round((low + high) / 2)

        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lst = [1, 3, 5, 7, 9]
print(binary_search(lst, 9))

```

This Python code implements a binary search algorithm for finding a specified element in a sorted list. It uses a while loop to keep narrowing the search until the specified element is found or until it is determined that the element does not exist. The `binary_search` function takes two arguments: a sorted list, `lst`, and the element to be found, `item`. if the specified element is found, it returns the index value of the element; otherwise it returns `None`.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/binary_search.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
4
```

At this point, your code is running successfully!
