# Definir uma função para obter o ponto de uma linha vertical rotacionada

Definiremos uma função que recebe as coordenadas da origem, o comprimento da linha e o ângulo em graus como entradas e retorna as coordenadas xy do final da linha vertical rotacionada pelo ângulo especificado.

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```
