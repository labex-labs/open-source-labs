# Criando um DataFrame (Quadro de Dados)

Os dados em pandas são armazenados em um DataFrame, que é uma estrutura de dados rotulada bidimensional com colunas potencialmente de diferentes tipos.

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
