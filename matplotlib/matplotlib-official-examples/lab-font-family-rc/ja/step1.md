# デフォルトのゴシック体フォントを選択する

Matplotlib のデフォルトのフォント ファミリはゴシック体です。`font.family` パラメータを `'sans-serif'` に設定することで、デフォルトのフォント ファミリを使用するように選択できます。これを行うには、次のコードを使用します。

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
```
