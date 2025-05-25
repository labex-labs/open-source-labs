# Criar Dados

Nesta etapa, criaremos alguns dados para plotar. Usaremos a função `squiggle_xy` para gerar algumas ondas senoidais e cossenoidais com diferentes frequências.

```python
def squiggle_xy(a, b, c, d):
    i = np.arange(0.0, 2*np.pi, 0.05)
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)
```
