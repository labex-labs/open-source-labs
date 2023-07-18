# Extract Specific Passenger Data

Next, let's extract the passenger data for the countesses on board of the Titanic. We'll use the `str.contains()` method to find rows where the `Name` column contains the word 'Countess'.

```python
# Find rows where 'Name' contains 'Countess'
countesses = titanic[titanic["Name"].str.contains("Countess")]
```
