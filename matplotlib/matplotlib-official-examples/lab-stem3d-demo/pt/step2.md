# Definir os dados

Nesta etapa, definiremos os dados que usaremos para criar o gráfico de hastes 3D. Criaremos um array linspace para o ângulo e usaremos as funções seno e cosseno para calcular as coordenadas x e y. Também definiremos a coordenada z como o ângulo.

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```
