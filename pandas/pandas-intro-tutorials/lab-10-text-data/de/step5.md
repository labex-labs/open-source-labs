# Finde den längsten Namen

Lassen Sie uns herausfinden, welcher Passagier der Titanic den längsten Namen hat. Wir verwenden die Methode `str.len()`, um die Länge jedes Namens zu erhalten, und die Methode `idxmax()`, um den Index des längsten Namens zu finden.

```python
# Get the length of each name
name_lengths = titanic["Name"].str.len()

# Find the index of the longest name
longest_name_index = name_lengths.idxmax()

# Get the longest name
longest_name = titanic.loc[longest_name_index, "Name"]
```
