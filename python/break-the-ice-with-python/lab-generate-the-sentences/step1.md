# Generate the Sentences

Please write a program to generate all sentences where subject is in `["I", "You"]` and verb is in `["Play", "Love"]` and the object is in `["Hockey","Football"]`.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/generate_the_sentences.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def generate_the_sentences():
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]

    for sub in subjects:
        for verb in verbs:
            for obj in objects:
                print("{} {} {}".format(sub, verb, obj))


generate_the_sentences()

```

This Python code defines a function called `generate_the_sentences`. Within the function, three lists are defined: `subjects`, `verbs`, and `objects`.

The `subjects` list contains two elements: "I" and "You". The `verbs` list contains two elements: "Play" and "Love". The `objects` list contains two elements: "Hockey" and "Football".

The function then uses three nested `for` loops to iterate over all possible combinations of subject, verb, and object. For each combination, a sentence is constructed using the `format` method and printed to the console using the `print` function.

Overall, this code demonstrates how to use nested `for` loops in Python to generate all possible combinations of elements from multiple lists, and how to use the `format` method to construct sentences from these combinations.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/generate_the_sentences.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football
```

At this point, your code is running successfully!
