# Criar o Gráfico de Barras

Agora, podemos criar o gráfico de barras usando os dados que definimos no Passo 2. Usaremos o método `bar()` do módulo `pyplot` do Matplotlib para criar o gráfico. Também passaremos os parâmetros `label` e `color` para controlar as entradas da legenda e as cores das barras, respectivamente. O código a seguir demonstra como criar o gráfico de barras:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```
