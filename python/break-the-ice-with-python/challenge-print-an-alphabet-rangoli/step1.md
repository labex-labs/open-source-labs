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

## Hints

- First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.
