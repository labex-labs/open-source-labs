# Sort Table Rows

Sort the Titanic dataset according to the age of the passengers and then by cabin class and age in descending order.

```python
# Sort by Age
titanic.sort_values(by="Age").head()

# Sort by Pclass and Age in descending order
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```
