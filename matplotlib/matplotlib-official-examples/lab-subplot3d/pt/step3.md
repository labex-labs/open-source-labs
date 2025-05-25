# Criar o Gráfico de Superfície 3D

Criaremos um gráfico de superfície 3D para o primeiro subplot. Usaremos NumPy para criar os dados para o gráfico.

```python
# Criar dados para o gráfico de superfície 3D
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plotar o gráfico de superfície 3D
surf = ax1.plot_surface(X, Y, Z, cmap='coolwarm', linewidth=0, antialiased=False)

# Adicionar uma barra de cores ao gráfico
fig.colorbar(surf, shrink=0.5, aspect=10)

# Definir os limites para o eixo z
ax1.set_zlim(-1.01, 1.01)
```
