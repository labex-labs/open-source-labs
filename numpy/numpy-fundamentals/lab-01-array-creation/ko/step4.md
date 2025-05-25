# 디스크에서 배열 읽기

다양한 형식으로 디스크에서 배열을 읽을 수 있습니다. 표준 바이너리 형식의 경우 HDF5 를 위한 h5py 및 FITS 를 위한 Astropy 와 같은 Python 라이브러리가 있습니다. CSV 및 TSV 와 같은 일반적인 ASCII 형식의 경우 `np.loadtxt` 및 `np.genfromtxt` 함수를 사용할 수 있습니다. 다음은 CSV 파일을 읽는 예시입니다.

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```
