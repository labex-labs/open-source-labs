# 結果のプロットと解釈

最後のステップは、結果をプロットして解釈することです。アルゴリズムの性能は、偽陽性率（FPR）が低い値のときの真陽性率（TPR）がどれだけ良いかに関係します。最良のアルゴリズムは、プロットの左上に曲線があり、曲線下の面積（AUC）が1に近いものです。対角線の破線は、アウトライアとインライアのランダムな分類を表します。

```python
import math
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

datasets_name = [
    "http",
    "smtp",
    "SA",
    "SF",
    "forestcover",
    "glass",
    "wdbc",
    "cardiotocography",
]

models_name = [
    "LOF",
    "IForest",
]

# プロットパラメータ
cols = 2
linewidth = 1
pos_label = 0  # 平均的に0は陽性クラスに属する
rows = math.ceil(len(datasets_name) / cols)

fig, axs = plt.subplots(rows, cols, figsize=(10, rows * 3), sharex=True, sharey=True)

for i, dataset_name in enumerate(datasets_name):
    (X, y) = preprocess_dataset(dataset_name=dataset_name)

    for model_idx, model_name in enumerate(models_name):
        y_pred = compute_prediction(X, model_name=model_name)
        display = RocCurveDisplay.from_predictions(
            y,
            y_pred,
            pos_label=pos_label,
            name=model_name,
            linewidth=linewidth,
            ax=axs[i // cols, i % cols],
            plot_chance_level=(model_idx == len(models_name) - 1),
            chance_level_kw={
                "linewidth": linewidth,
                "linestyle": ":",
            },
        )
    axs[i // cols, i % cols].set_title(dataset_name)
plt.tight_layout(pad=2.0)  # サブプロット間の間隔
plt.show()
```
