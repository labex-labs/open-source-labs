# 特定の等幅フォントを選択する

特定の等幅フォントを使用したい場合、`font.monospace` パラメータをフォント名のリストに設定できます。Matplotlib は、ユーザーのシステムで利用可能なリストの最初のフォントを使用しようとします。これを行うには、次のコードを使用します。

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
plt.rcParams["font.monospace"] = ["FreeMono"]
```
