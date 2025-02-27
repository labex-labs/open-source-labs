# パイプラインの作成

次に、特徴選択変換、スケーラー、およびSVMのインスタンスから構成されるパイプラインを作成します。これらを組み合わせて、完全な推定器を作成します。

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

clf = Pipeline(
    [
        ("anova", SelectPercentile(f_classif)),
        ("scaler", StandardScaler()),
        ("svc", SVC(gamma="auto")),
    ]
)
```
