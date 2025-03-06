# デフォルトのタイトル位置での基本的なプロット作成

このステップでは、単純な折れ線グラフを作成し、中央に配置されたタイトルを追加します。これは Matplotlib でのデフォルトの位置です。

## Jupyter Notebook の作成

VM の起動が完了したら、左上隅をクリックして **Notebook** タブに切り替え、Jupyter Notebook にアクセスします。

![click-notebook](https://file.labex.io/images/click-notebook.png)

Jupyter Notebook の読み込みが完了するまで数秒待つ必要がある場合があります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

実験中に何か問題が発生した場合は、いつでも Labby に支援を求めてください。セッション終了後にフィードバックを提供していただければ、問題を迅速に解決できます。

## Matplotlib のインポート

では、まず Matplotlib ライブラリをインポートしましょう。ノートブックの最初のセルに以下のコードを入力し、Shift+Enter を押して実行します。

```python
import matplotlib.pyplot as plt
```

これにより、Matplotlib から pyplot モジュールがインポートされ、一般的な慣例に従って `plt` というエイリアスが割り当てられます。

## 単純なプロットの作成

次に、基本的な折れ線グラフを作成しましょう。新しいセルに以下のコードを入力して実行します。

```python
plt.figure(figsize=(8, 5))  # Create a figure with a specific size
plt.plot(range(10))         # Plot numbers from 0 to 9
plt.grid(True)              # Add a grid for better readability
plt.show()                  # Display the plot
```

出力には 0 から 9 までの値が表示された単純な折れ線グラフが表示されるはずです。

![line-plot](../assets/screenshot-20250306-g5knGobR@2x.png)

## デフォルト（中央）のタイトルの追加

では、プロットにタイトルを追加しましょう。タイトルのデフォルトの位置は、プロットの上部中央です。新しいセルに以下のコードを入力します。

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('My First Matplotlib Plot')  # Add a centered title
plt.show()
```

![line-plot-with-title](../assets/screenshot-20250306-XMODABB2@2x.png)

セルを実行すると、上部に中央配置されたタイトルが付いたプロットが表示されるはずです。

追加のパラメータを指定せずに `title()` 関数を使用すると、タイトルはデフォルトの位置である中央に配置されます。
