# 欠損値の処理と埋め込み

`missing_values` 引数と `filling_values` 引数は、欠損データを処理するために使用されます。`missing_values` 引数は欠損データを認識するために使用され、`filling_values` 引数は欠損エントリに対する値を提供するために使用されます。

```python
np.genfromtxt(StringIO(data), missing_values="N/A", filling_values=0)
```
