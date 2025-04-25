# サイン波関数の定義

次に、サイン波を生成する関数を定義します。この関数は 2 つのパラメータ、振幅と周波数を受け取り、与えられた時刻におけるサイン波を返します。

```python
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
```
