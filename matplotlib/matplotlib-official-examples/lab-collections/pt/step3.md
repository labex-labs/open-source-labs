# Criar deslocamentos (offsets)

```python
# Fixing random state for reproducibility
rs = np.random.RandomState(19680801)

# Make some offsets
xyo = rs.randn(npts, 2)
```

O terceiro passo é criar deslocamentos usando Numpy. Usaremos a função random para criar os deslocamentos.
