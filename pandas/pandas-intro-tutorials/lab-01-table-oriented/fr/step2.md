# Créez un DataFrame

Les données dans pandas sont stockées dans un DataFrame, qui est une structure de données étiquetée en 2 dimensions avec des colonnes potentiellement de différents types.

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
