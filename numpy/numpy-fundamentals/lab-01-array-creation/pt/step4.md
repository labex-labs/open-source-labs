# Lendo Arrays do Disco

Você pode ler arrays do disco em vários formatos. Para formatos binários padrão, existem bibliotecas Python como h5py para HDF5 e Astropy para FITS. Para formatos ASCII comuns como CSV e TSV, você pode usar as funções `np.loadtxt` e `np.genfromtxt`. Aqui está um exemplo de leitura de um arquivo CSV:

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```
