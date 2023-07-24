# Sort the Tuples

You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

- **_1: Sort based on name_**
- **_2: Then sort based on age_**
- **_3: Then sort by score_**

The priority is that name > age > score.

## Example

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

## Hints

- In case of input data being supplied to the program, it should be assumed to be a console input.We use itemgetter to enable multiple sort keys.
