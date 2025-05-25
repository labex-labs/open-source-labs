# Criando o Caminho (Path)

Em seguida, criaremos o objeto `Path` para a Curva de Bézier. O objeto `Path` recebe uma lista de vértices e códigos que especificam o tipo de caminho entre os vértices. Neste caso, usaremos um código `MOVETO` para mover para o ponto inicial, seguido por dois códigos `CURVE3` para especificar os pontos de controle e o ponto final, e finalmente um código `CLOSEPOLY` para fechar o caminho.

```python
Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])
```
