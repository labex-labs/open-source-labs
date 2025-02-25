# Usando declaraciones if/verdad con Pandas

Pandas no admite el uso directo de declaraciones if/verdad debido a la ambigüedad. En su lugar, utilice métodos como `.any()`, `.all()` o `.empty()`.

```python
# Comprueba si algún valor en la Serie es True
if pd.Series([False, True, False]).any():
    print("Al menos un valor True en la Serie")
```
