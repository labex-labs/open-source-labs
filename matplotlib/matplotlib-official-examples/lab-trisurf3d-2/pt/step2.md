# Criar uma Malha

Criamos uma malha no espaço das variáveis de parametrização `u` e `v`. Isso é feito usando a função `np.meshgrid()` para criar uma grade de pontos `u` e `v`.

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```
