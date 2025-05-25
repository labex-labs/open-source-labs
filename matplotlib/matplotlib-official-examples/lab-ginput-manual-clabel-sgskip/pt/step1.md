# Definir um Triângulo Clicando em Três Pontos

Nesta etapa, definiremos um triângulo clicando em três pontos. Usaremos as funções `ginput` e `waitforbuttonpress` para conseguir isso. A função `ginput` nos permite selecionar pontos no gráfico com o mouse, e a função `waitforbuttonpress` aguarda um evento de pressionamento de botão.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()

plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)

tellme('Você definirá um triângulo, clique para começar')

plt.waitforbuttonpress()

while True:
    pts = []
    while len(pts) < 3:
        tellme('Selecione 3 cantos com o mouse')
        pts = np.asarray(plt.ginput(3, timeout=-1))
        if len(pts) < 3:
            tellme('Pontos insuficientes, começando de novo')
            time.sleep(1)  # Aguarda um segundo

    ph = plt.fill(pts[:, 0], pts[:, 1], 'r', lw=2)

    tellme('Feliz? Clique em uma tecla para sim, clique com o mouse para não')

    if plt.waitforbuttonpress():
        break

    # Get rid of fill
    for p in ph:
        p.remove()
```
