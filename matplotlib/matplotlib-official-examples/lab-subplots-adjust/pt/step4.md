# Ajustar a Posição da Barra de Cores

Também podemos ajustar a posição da barra de cores usando `plt.axes`. Esta função recebe uma lista de valores `[left, bottom, width, height]` como argumentos para especificar a posição e o tamanho dos eixos (axes). Execute o seguinte código:

```python
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)
```
