# Exemplo Prático - Quantização Vetorial

Vamos explorar um exemplo prático onde o broadcasting (difusão) é útil. Considere o algoritmo de quantização vetorial (VQ - _Vector Quantization_) usado na teoria da informação e classificação. A operação básica em VQ é encontrar o ponto mais próximo em um conjunto de pontos a um determinado ponto. Isso pode ser feito usando broadcasting. Aqui está um exemplo:

```python
import numpy as np

observation = np.array([111.0, 188.0])
codes = np.array([[102.0, 203.0],
                  [132.0, 193.0],
                  [45.0, 155.0],
                  [57.0, 173.0]])
diff = codes - observation
dist = np.sqrt(np.sum(diff**2, axis=-1))
closest_index = np.argmin(dist)
closest_code = codes[closest_index]
```

Neste exemplo, `observation` representa o peso e a altura de um atleta a ser classificado, e `codes` representa diferentes classes de atletas. Subtraindo `observation` de `codes`, o broadcasting é usado para calcular a distância entre `observation` e cada um dos códigos. A função `argmin` é então usada para encontrar o índice do código mais próximo.
