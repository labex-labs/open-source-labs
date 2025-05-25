# Criar a Chave de Quiver

Podemos adicionar uma chave de quiver ao gráfico para mostrar a escala das setas. Usamos a função `ax.quiverkey()` para adicionar a chave. Passamos o objeto `q`, a posição `X` e `Y` da chave, o comprimento da seta, o rótulo para a chave e a posição do rótulo.

```python
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')
```
