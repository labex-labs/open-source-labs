# Extract Substrings

You can extract substrings using regular expressions. The `extract` method accepts a regular expression with at least one capture group.

```python
# extract the first digit from each string
s = pd.Series(["a1", "b2", "c3"], dtype="string")
s.str.extract(r"(\d)", expand=False)
```
