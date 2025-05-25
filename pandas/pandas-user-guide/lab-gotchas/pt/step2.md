# Usando Instruções if/truth com Pandas

O Pandas não suporta o uso direto de instruções if/truth devido à ambiguidade. Em vez disso, use métodos como `.any()`, `.all()` ou `.empty()`.

```python
# Check if any value in the Series is True
if pd.Series([False, True, False]).any():
    print("At least one True value in the Series")
```
