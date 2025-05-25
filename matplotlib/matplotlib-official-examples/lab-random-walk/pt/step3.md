# Definir a Função de Atualização

Definimos uma função que atualiza o gráfico para cada quadro da animação. A função recebe três entradas: `num` é o número do quadro atual, `walks` é uma lista de todos os passeios aleatórios e `lines` é uma lista de todas as linhas no gráfico. Para cada linha e passeio, atualizamos os dados para as coordenadas x, y e z da linha até o número do quadro atual. Usamos `line.set_data()` e `line.set_3d_properties()` para atualizar as coordenadas x-y e z, respectivamente.

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```
