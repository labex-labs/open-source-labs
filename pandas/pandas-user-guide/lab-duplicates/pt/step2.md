# Compreendendo as Consequências de Rótulos Duplicados

Rótulos duplicados podem alterar o comportamento de certas operações em pandas. Por exemplo, alguns métodos não funcionam quando há duplicatas presentes.

```python
# Criando uma pandas Series com rótulos duplicados
s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])

# Tentando reindexar a Series
try:
    s1.reindex(["a", "b", "c"])
except Exception as e:
    print(e)
```
