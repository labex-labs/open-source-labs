# Replace Values in a Column

Finally, let's replace the values in the `Sex` column: 'male' with 'M' and 'female' with 'F'. We'll use the `replace()` method for this.

```python
# Replace 'male' with 'M' and 'female' with 'F' in the 'Sex' column
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
```
