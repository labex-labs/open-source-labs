# Criar o Eixo Secundário

Agora criaremos o eixo secundário e converteremos o eixo x de graus para radianos. Usaremos `deg2rad` como a função direta (forward function) e `rad2deg` como a função inversa (inverse function).

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('angle [rad]')
```
