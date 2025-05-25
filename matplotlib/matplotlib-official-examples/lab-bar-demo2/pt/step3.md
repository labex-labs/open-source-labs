# Criar o Gráfico de Barras com Unidades Padrão

Nesta etapa, criaremos o gráfico de barras com unidades padrão usando o método `bar` do Matplotlib. Usaremos o parâmetro `bottom` para definir a base das barras como 0.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].bar(cms, cms, bottom=bottom)
```
