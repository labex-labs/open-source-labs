# Ajustar os Limites e Adicionar Rótulos

Finalmente, ajustaremos os limites do gráfico e adicionaremos rótulos aos eixos usando as funções `set_zlim()`, `set_xlabel()`, `set_ylabel()` e `set_zlabel()` do Matplotlib. Também usaremos o modo matemático LaTeX para escrever os rótulos dos eixos.

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```
