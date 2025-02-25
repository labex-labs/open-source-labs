# Чтение массивов с диска

Массивы можно читать с диска в различных форматах. Для стандартных двоичных форматов существуют библиотеки Python, такие как h5py для HDF5 и Astropy для FITS. Для общих ASCII-форматов, таких как CSV и TSV, можно использовать функции `np.loadtxt` и `np.genfromtxt`. Вот пример чтения CSV-файла:

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```
