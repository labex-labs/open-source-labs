# Usando Métodos de String

O pandas fornece um conjunto de métodos de processamento de string que facilitam a operação em dados de string. Esses métodos excluem automaticamente valores ausentes/NA.

```python
s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

# convert to lowercase
s.str.lower()

# convert to uppercase
s.str.upper()

# calculate the length of each string
s.str.len()
```
