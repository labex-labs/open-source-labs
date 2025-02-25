# 特定のゴシック体フォントを選択する

特定のゴシック体フォントを使用したい場合、`font.sans-serif` パラメータをフォント名のリストに設定できます。Matplotlib は、ユーザーのシステムで利用可能なリストの最初のフォントを使用しようとします。これを行うには、次のコードを使用します。

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Nimbus Sans"]
```
