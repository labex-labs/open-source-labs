# Plotar o dendrograma

Plotaremos o dendrograma usando a função `dendrogram()` do módulo `scipy.cluster.hierarchy` e a função `plot_dendrogram()` definida no código original.

```python
plt.title("Dendrograma de Agrupamento Hierárquico")
plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Número de pontos no nó (ou índice do ponto se não houver parênteses).")
plt.show()
```
