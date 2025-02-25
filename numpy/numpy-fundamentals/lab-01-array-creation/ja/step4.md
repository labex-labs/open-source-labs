# ディスクから配列を読み込む

ディスクから配列を様々な形式で読み込むことができます。標準のバイナリ形式では、HDF5 用の h5py や FITS 用の Astropy などの Python ライブラリがあります。CSV や TSV などの一般的な ASCII 形式では、`np.loadtxt` と `np.genfromtxt` 関数を使用できます。以下は CSV ファイルを読み込む例です。

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```
