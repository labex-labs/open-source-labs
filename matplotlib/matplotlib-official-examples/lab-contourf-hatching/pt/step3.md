# Gráfico Hachurado Mais Simples com uma Barra de Cores

Nesta etapa, criaremos o gráfico hachurado mais simples com uma barra de cores. Usaremos a função `contourf` para criar o gráfico de contorno preenchido e especificaremos as hachuras usando o parâmetro `hatches`.

```python
fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches=['-', '/', '\\', '//'],
                  cmap='gray', extend='both', alpha=0.5)
fig1.colorbar(cs)
```
