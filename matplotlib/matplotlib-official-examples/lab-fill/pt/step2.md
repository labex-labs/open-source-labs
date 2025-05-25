# Definir a Função do Floco de Neve de Koch

Em seguida, definiremos uma função para gerar o floco de neve de Koch. A função recebe dois parâmetros: a profundidade de recursão e o fator de escala.

```python
def koch_snowflake(order, scale=10):
    """
    Retorna duas listas x, y de coordenadas de pontos do floco de neve de Koch.

    Parâmetros
    ----------
    order : int
        A profundidade de recursão.
    scale : float
        A extensão do floco de neve (comprimento da aresta do triângulo base).
    """
    def _koch_snowflake_complex(order):
        if order == 0:
            # initial triangle
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)  # start points
            p2 = np.roll(p1, shift=-1)  # end points
            dp = p2 - p1  # connection vectors

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y
```
