# Gerando um conjunto de dados

Criamos um conjunto de dados sintético. O verdadeiro processo gerador receberá um vetor 1-D e calculará seu seno.

```python
import numpy as np

rng = np.random.RandomState(0)
data = np.linspace(0, 30, num=1_000).reshape(-1, 1)
target = np.sin(data).ravel()

training_sample_indices = rng.choice(np.arange(0, 400), size=40, replace=False)
training_data = data[training_sample_indices]
training_noisy_target = target[training_sample_indices] + 0.5 * rng.randn(
    len(training_sample_indices)
)
```
