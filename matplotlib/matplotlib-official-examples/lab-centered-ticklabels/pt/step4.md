# Remover os Rótulos das Marcas Principais e as Marcas Secundárias

Para simular o comportamento de centralização dos rótulos entre as marcas (ticks), precisamos remover os rótulos das marcas principais e as marcas secundárias e mostrar apenas os rótulos das marcas secundárias. Podemos fazer isso usando a função `tick_params()` e definindo os parâmetros `tick1On` e `tick2On` como `False`.

```python
# Remove the tick lines
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
```
