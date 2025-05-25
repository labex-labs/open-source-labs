# Plotando a Dependência Parcial dos Dois Modelos Juntos

Neste passo, plotaremos as curvas de dependência parcial dos dois modelos no mesmo gráfico.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("Árvore de Decisão")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("Perceptron Multicamadas")
```

Outra forma de comparar as curvas é plotá-las uma sobre a outra. Aqui, criamos uma figura com uma linha e duas colunas. Os eixos são passados para a função `PartialDependenceDisplay.plot` como uma lista, o que plotará as curvas de dependência parcial de cada modelo nos mesmos eixos. O comprimento da lista de eixos deve ser igual ao número de gráficos desenhados.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "Árvore de Decisão"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "Perceptron Multicamadas", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_` é um contêiner do tipo numpy array que contém os eixos usados para desenhar os gráficos de dependência parcial. Isso pode ser passado para `mlp_disp` para ter o mesmo efeito de desenhar os gráficos um sobre o outro. Além disso, `mlp_disp.figure_` armazena a figura, o que permite redimensionar a figura após a chamada de `plot`. Neste caso, `tree_disp.axes_` tem duas dimensões, portanto, `plot` mostrará apenas a legenda e os ticks do eixo y no gráfico mais à esquerda.

```python
tree_disp.plot(line_kw={"label": "Árvore de Decisão"})
mlp_disp.plot(
    line_kw={"label": "Perceptron Multicamadas", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```
