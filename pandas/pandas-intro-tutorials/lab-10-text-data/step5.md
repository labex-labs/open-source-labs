# Find the Longest Name

Let's find out which passenger of the Titanic has the longest name. We'll use the `str.len()` method to get the length of each name, and the `idxmax()` method to find the index of the longest name.

```python
# Get the length of each name
name_lengths = titanic["Name"].str.len()

# Find the index of the longest name
longest_name_index = name_lengths.idxmax()

# Get the longest name
longest_name = titanic.loc[longest_name_index, "Name"]
```
