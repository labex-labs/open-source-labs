# Word Counting

You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

## Example

If the following string is given as input to the program:

```bash
4
bcdef
abcdefg
bcde
bcdef
```

Then, the output of the program should be:

```bash
3
2 1 1
```

## Hints

- Make a list to get the input order and a dictionary to count the word frequency
