# Criar a figura 3D e os dados

Nesta etapa, criaremos uma figura 3D e obteremos dados de teste para o gráfico de superfície.

```python
# Criar uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Obter dados de teste para o gráfico de superfície
X, Y, Z = axes3d.get_test_data(0.05)
```
