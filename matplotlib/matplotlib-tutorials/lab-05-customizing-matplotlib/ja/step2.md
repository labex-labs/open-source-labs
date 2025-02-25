# スタイル シートの使用

グラフの視覚的な外観を変更する別の方法は、スタイル シートで rcParams を設定し、`matplotlib.style.use` を使ってそのスタイル シートをインポートすることです。スタイル シートは、グラフのスタイルに関連する一連の rcParams を含むファイルです。Matplotlib は、使用できるいくつかの事前定義済みのスタイルを提供しています。たとえば、「ggplot」スタイルは R の ggplot ライブラリの美学をエミュレートします。このようにしてスタイル シートを適用できます：

```python
import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('Solarize_Light2')
```

独自のカスタム スタイルを定義し、それをスタイル シートのパスまたは URL を指定して `.style.use` を呼び出すことで使用することもできます。
