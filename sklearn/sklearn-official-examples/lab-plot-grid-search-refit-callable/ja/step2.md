# 関数の定義

この実験の後で使用される 2 つの関数を定義します。

```python
def lower_bound(cv_results):
    """
    最良の `mean_test_scores` の 1 標準偏差以内の下限を計算します。

    パラメータ
    ----------
    cv_results : numpy(masked) ndarrays の辞書
        `GridSearchCV` の cv_results_ 属性を参照してください

    戻り値
    -------
    float
        最良の `mean_test_score` の 1 標準偏差以内の下限
    """
    best_score_idx = np.argmax(cv_results["mean_test_score"])

    return (
        cv_results["mean_test_score"][best_score_idx]
        - cv_results["std_test_score"][best_score_idx]
    )


def best_low_complexity(cv_results):
    """
    交差検証スコアとモデルの複雑さをバランスさせます。

    パラメータ
    ----------
    cv_results : numpy(masked) ndarrays の辞書
        `GridSearchCV` の cv_results_ 属性を参照してください。

    戻り値
    ------
    int
        最良の `mean_test_score` の 1 標準偏差以内のテストスコアを持ちながら、最も少ない PCA コンポーネントを持つモデルのインデックス
    """
    threshold = lower_bound(cv_results)
    candidate_idx = np.flatnonzero(cv_results["mean_test_score"] >= threshold)
    best_idx = candidate_idx[
        cv_results["param_reduce_dim__n_components"][candidate_idx].argmin()
    ]
    return best_idx
```
