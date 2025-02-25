# Erstellen eines DataFrames

Die Daten in pandas werden in einem DataFrame gespeichert, das eine zweidimensionale gelabelte Datenstruktur ist, deren Spalten möglicherweise unterschiedlicher Typen sind.

```python
# Creating a DataFrame
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
```
