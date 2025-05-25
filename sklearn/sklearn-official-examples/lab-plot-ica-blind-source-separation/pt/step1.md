# Gerar Dados de Amostra

Vamos gerar um sinal misto de amostra composto por três componentes independentes. Adicionaremos ruído ao sinal e padronizaremos os dados. Também geraremos uma matriz de mistura para misturar nossos três componentes independentes.

```python
import numpy as np
from scipy import signal

np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * time)  # Sinal 1: sinal sinusoidal
s2 = np.sign(np.sin(3 * time))  # Sinal 2: sinal quadrado
s3 = signal.sawtooth(2 * np.pi * time)  # Sinal 3: sinal dente de serra

S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # Adicionar ruído

S /= S.std(axis=0)  # Padronizar os dados
# Misturar dados
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # Matriz de mistura
X = np.dot(S, A.T)  # Gerar observações
```
