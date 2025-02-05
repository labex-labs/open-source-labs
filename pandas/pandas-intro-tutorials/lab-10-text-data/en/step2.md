# Convert String Characters to Lowercase

Next, we will convert all characters in the `Name` column to lowercase. We'll use the `str.lower()` method to achieve this.

```python
# Convert all characters in the 'Name' column to lowercase
titanic["Name"] = titanic["Name"].str.lower()
```
