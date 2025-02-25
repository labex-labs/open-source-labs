# 単一のサブプロット付きの図の作成

単一のサブプロットを作成する最も簡単な方法は、引数なしで`subplots()`関数を使用することです。この関数は`Figure`オブジェクトと単一の`Axes`オブジェクトを返します。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

```
