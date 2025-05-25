# Definir o formatador e o localizador de marcas de escala (tick)

Definimos o formatador de marcas de escala (tick formatter) do eixo x para a função de formatação criada no Passo 5 usando o método `set_major_formatter()`. Também definimos o localizador de marcas de escala (tick locator) do eixo x para `MaxNLocator(integer=True)` para garantir que os valores das marcas de escala assumam valores inteiros.

```python
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```
