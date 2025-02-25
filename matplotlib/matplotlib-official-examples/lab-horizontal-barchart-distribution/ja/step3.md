# 関数の定義

ここで、`results` と `category_names` を引数に取り、水平積み上げバーチャートの可視化を作成する `survey` という関数を定義します。

```python
def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        質問ラベルから各カテゴリごとの回答のリストへのマッピング。
        すべてのリストが同じ数のエントリを含み、*category_names* の長さと一致すると仮定されます。
    category_names : list of str
        カテゴリのラベル。
    """
    # 結果とカテゴリをnumpy配列に変換
    labels = list(results.keys())
    data = np.array(list(results.values()))

    # 水平積み上げ用にデータの累積和を計算
    data_cum = data.cumsum(axis=1)

    # カテゴリの色を定義
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    # プロットを作成して軸のプロパティを設定
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    # 積み上げバーを作成してバーのラベルを追加
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # 凡例を追加
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
```
