# Desativar os Rótulos de Marcação (Tick Labels)

Para remover os rótulos de marcação de cada um dos _insets_, podemos usar o método `tick_params()` e definir `labelleft` e `labelbottom` como `False`.

```python
# Desativar os ticklabels dos insets
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```
