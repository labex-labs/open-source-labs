# Criar o Gráfico Wireframe 3D

Criaremos um gráfico wireframe 3D para o segundo subplot. Usaremos a função `get_test_data` de `mpl_toolkits.mplot3d.axes3d` para criar os dados para o gráfico.

```python
# Criar dados para o gráfico wireframe 3D
X, Y, Z = Axes3D.get_test_data(0.05)

# Plotar o gráfico wireframe 3D
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
