# 分類器のベンチマーク

ここでは、8つの異なる分類モデルを使ってデータセットを訓練とテストし、各モデルの性能結果を取得します。この研究の目的は、このような多クラスのテキスト分類問題に対する異なる種類の分類器の計算量/精度のトレードオフを明らかにすることです。

```python
from sklearn.utils.extmath import density
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import ComplementNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier

results = []
for clf, name in (
    (LogisticRegression(C=5, max_iter=1000), "ロジスティック回帰"),
    (RidgeClassifier(alpha=1.0, solver="sparse_cg"), "リッジ分類器"),
    (KNeighborsClassifier(n_neighbors=100), "kNN"),
    (RandomForestClassifier(), "ランダムフォレスト"),
    # L2ペナルティ付きの線形SVC
    (LinearSVC(C=0.1, dual=False, max_iter=1000), "線形SVC"),
    # L2ペナルティ付きの線形SGD
    (
        SGDClassifier(
            loss="log_loss", alpha=1e-4, n_iter_no_change=3, early_stopping=True
        ),
        "log-loss SGD",
    ),
    # 最近傍重心法（つまりロッキオ分類器）
    (NearestCentroid(), "最近傍重心法"),
    # 疎なナイーブベイズ分類器
    (ComplementNB(alpha=0.1), "補完ナイーブベイズ"),
):
    print("=" * 80)
    print(name)
    results.append(benchmark(clf, name))

indices = np.arange(len(results))

results = [[x[i] for x in results] for i in range(4)]

clf_names, score, training_time, test_time = results
training_time = np.array(training_time)
test_time = np.array(test_time)

fig, ax1 = plt.subplots(figsize=(10, 8))
ax1.scatter(score, training_time, s=60)
ax1.set(
    title="Score-training time trade-off",
    yscale="log",
    xlabel="テスト精度",
    ylabel="訓練時間 (秒)",
)
fig, ax2 = plt.subplots(figsize=(10, 8))
ax2.scatter(score, test_time, s=60)
ax2.set(
    title="Score-test time trade-off",
    yscale="log",
    xlabel="テスト精度",
    ylabel="テスト時間 (秒)",
)

for i, txt in enumerate(clf_names):
    ax1.annotate(txt, (score[i], training_time[i]))
    ax2.annotate(txt, (score[i], test_time[i]))
```
