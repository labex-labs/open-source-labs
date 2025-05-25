# 결과 플롯 및 해석

마지막 단계는 결과를 플롯하고 해석하는 것입니다. 알고리즘의 성능은 거짓 양성률 (FPR) 이 낮은 값에서 진짜 양성률 (TPR) 이 얼마나 좋은지에 따라 결정됩니다. 최상의 알고리즘은 플롯의 왼쪽 상단에 곡선이 있고 곡선 아래 면적 (AUC) 이 1 에 가깝습니다. 대각선 점선은 이상치와 내부 데이터의 무작위 분류를 나타냅니다.

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

# 플롯 매개변수
cols = 2
linewidth = 1
pos_label = 0  # 0 이 양성 클래스에 속함을 의미
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
plt.tight_layout(pad=2.0)  # 서브플롯 간 간격
plt.show()
```
