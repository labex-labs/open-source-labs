# 定义函数

我们将定义两个稍后在实验中会用到的函数。

```python
def lower_bound(cv_results):
    """
    计算最佳 `mean_test_scores` 的 1 个标准差范围内的下限。

    参数
    ----------
    cv_results : numpy（掩码）ndarray 的字典
        请参阅 `GridSearchCV` 的 cv_results_ 属性

    返回
    -------
    float
        最佳 `mean_test_score` 的 1 个标准差范围内的下限。
    """
    best_score_idx = np.argmax(cv_results["mean_test_score"])

    return (
        cv_results["mean_test_score"][best_score_idx]
        - cv_results["std_test_score"][best_score_idx]
    )


def best_low_complexity(cv_results):
    """
    平衡模型复杂度与交叉验证分数。

    参数
    ----------
    cv_results : numpy（掩码）ndarray 的字典
        请参阅 `GridSearchCV` 的 cv_results_ 属性。

    返回
    ------
    int
        具有最少 PCA 组件数量且其测试分数在最佳 `mean_test_score` 的 1 个标准差范围内的模型的索引。
    """
    threshold = lower_bound(cv_results)
    candidate_idx = np.flatnonzero(cv_results["mean_test_score"] >= threshold)
    best_idx = candidate_idx[
        cv_results["param_reduce_dim__n_components"][candidate_idx].argmin()
    ]
    return best_idx
```
