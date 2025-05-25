# Personalizar os Eixos

Agora, personalizaremos os eixos do gráfico 3D. Definiremos os rótulos para os eixos x, y e z usando os métodos `set_xlabel()`, `set_ylabel()` e `set_zlabel()`, respectivamente. Também definiremos os ticks no eixo y usando o método `set_yticks()`.

```python
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_yticks(yticks)
```
