# Criando os Dados

O próximo passo é criar os dados para a superfície 3D. Precisamos definir `u`, `v`, `x`, `y` e `z`. Essas variáveis representarão os ângulos e coordenadas necessários para plotar a superfície. A função `linspace()` do NumPy é usada para criar os ângulos, e a função `outer()` é usada para criar as coordenadas.

```python
# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
```
