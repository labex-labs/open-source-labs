# Alinhar os Rótulos das Marcas Secundárias

Finalmente, precisamos alinhar os rótulos das marcas secundárias ao centro entre as marcas principais. Podemos fazer isso usando a função `get_xticklabels()` e definindo o parâmetro `minor` como `True` para obter os rótulos das marcas secundárias. Em seguida, podemos iterar pelos rótulos e definir o alinhamento horizontal como `'center'`.

```python
# Align the minor tick label
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```
