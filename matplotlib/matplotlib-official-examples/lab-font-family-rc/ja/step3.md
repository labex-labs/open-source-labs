# デフォルトの等幅フォントを選択する

Matplotlib のデフォルトの等幅フォントはオペレーティング システムによって決まります。`font.family` パラメータを `'monospace'` に設定することで、デフォルトの等幅フォントを使用するように選択できます。これを行うには、次のコードを使用します。

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
```
