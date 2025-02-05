# Extract Surnames from Full Names

Now, let's create a new column `Surname` that contains the surname of the passengers. We'll achieve this by extracting the part before the comma in the `Name` column.

```python
# Split the 'Name' column on comma and extract the first part
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
```
