# Análise de Componentes Independentes (ICA)

#### ICA para separação de fontes cegas

A Análise de Componentes Independentes (ICA) é usada para separar sinais mistos em seus componentes de fonte originais. Supõe-se que os componentes são estatisticamente independentes e podem ser extraídos por meio de um processo linear de desmistura. A ICA pode ser implementada usando a classe `FastICA` do scikit-learn.

```python
from sklearn.decomposition import FastICA

# Crie um objeto ICA com n_components como o número de componentes desejados
ica = FastICA(n_components=2)

# Ajuste o modelo ICA aos sinais mistos
ica.fit(mixed_signals)

# Separe os sinais mistos nos componentes de fonte originais
source_components = ica.transform(mixed_signals)
```
