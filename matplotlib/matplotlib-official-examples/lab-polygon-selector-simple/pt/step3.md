# Criar um Polígono Interativamente

Para criar um polígono interativamente, precisamos criar um objeto `Figure` e um objeto `Axes`. Em seguida, podemos criar um objeto `PolygonSelector` e adicionar vértices a ele clicando no gráfico. Também podemos usar as teclas `shift` e `ctrl` para mover os vértices.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("Clique na figura para criar um polígono.")
print("Pressione a tecla 'esc' para iniciar um novo polígono.")
print("Tente segurar a tecla 'shift' para mover todos os vértices.")
print("Tente segurar a tecla 'ctrl' para mover um único vértice.")

plt.show()
```
