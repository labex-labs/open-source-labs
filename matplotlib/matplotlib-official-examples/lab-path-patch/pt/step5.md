# Plotar Pontos de Controle e Linhas de Conexão

Nesta etapa, plotamos os pontos de controle e as linhas de conexão do caminho usando o método `plot` do objeto axes.

```python
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
```
