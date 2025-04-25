# 基本的なプロットの作成

まずは、テキスト要素付きの基本的なプロットを作成してみましょう。Python スクリプトに次のコードを追加します。

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```
