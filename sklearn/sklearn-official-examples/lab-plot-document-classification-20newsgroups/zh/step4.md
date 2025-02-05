# 对分类器进行基准测试

现在我们将使用八个不同的分类模型对数据集进行训练和测试，并获取每个模型的性能结果。本研究的目的是突出针对此类多类别文本分类问题，不同类型分类器在计算量/准确性方面的权衡。

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
    (LogisticRegression(C=5, max_iter=1000), "逻辑回归"),
    (RidgeClassifier(alpha=1.0, solver="sparse_cg"), "岭分类器"),
    (KNeighborsClassifier(n_neighbors=100), "k近邻"),
    (RandomForestClassifier(), "随机森林"),
    # L2 惩罚的线性支持向量分类器
    (LinearSVC(C=0.1, dual=False, max_iter=1000), "线性支持向量分类器"),
    # L2 惩罚的线性随机梯度下降
    (
        SGDClassifier(
            loss="log_loss", alpha=1e-4, n_iter_no_change=3, early_stopping=True
        ),
        "对数损失随机梯度下降",
    ),
    # 最近质心（又名罗基奥分类器）
    (NearestCentroid(), "最近质心"),
    # 稀疏朴素贝叶斯分类器
    (ComplementNB(alpha=0.1), "互补朴素贝叶斯"),
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
    title="得分 - 训练时间权衡",
    yscale="log",
    xlabel="测试准确率",
    ylabel="训练时间（秒）",
)
fig, ax2 = plt.subplots(figsize=(10, 8))
ax2.scatter(score, test_time, s=60)
ax2.set(
    title="得分 - 测试时间权衡",
    yscale="log",
    xlabel="测试准确率",
    ylabel="测试时间（秒）",
)

for i, txt in enumerate(clf_names):
    ax1.annotate(txt, (score[i], training_time[i]))
    ax2.annotate(txt, (score[i], test_time[i]))
```
