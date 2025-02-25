# Создаем DataFrame

Данные в pandas хранятся в DataFrame, который представляет собой двухмерную структуру данных с метками, в которой столбцы могут иметь разные типы.

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
