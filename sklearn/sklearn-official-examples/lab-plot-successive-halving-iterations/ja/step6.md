# 結果の分析

探索オブジェクトの`cv_results_`属性には探索の結果が含まれています。以下のコードを使ってそれをpandasのデータフレームに変換します：

```python
results = pd.DataFrame(rsh.cv_results_)
```

`params_str`列は`params`列を文字列に変換することで作成されます。同じ`params_str`と`iter`値を持つ重複行を削除します：

```python
results["params_str"] = results.params.apply(str)
results.drop_duplicates(subset=("params_str", "iter"), inplace=True)
```

次に、平均テストスコアを`pivot`メソッドを使って反復回数とパラメータの組み合わせに対してピボットします：

```python
mean_scores = results.pivot(
    index="iter", columns="params_str", values="mean_test_score"
)
```

最後に、以下のコードを使って反復回数に対する平均テストスコアをプロットします：

```python
ax = mean_scores.plot(legend=False, alpha=0.6)

labels = [
    f"iter={i}\nn_samples={rsh.n_resources_[i]}\nn_candidates={rsh.n_candidates_[i]}"
    for i in range(rsh.n_iterations_)
]

ax.set_xticks(range(rsh.n_iterations_))
ax.set_xticklabels(labels, rotation=45, multialignment="left")
ax.set_title("Scores of candidates over iterations")
ax.set_ylabel("mean test score", fontsize=15)
ax.set_xlabel("iterations", fontsize=15)
plt.tight_layout()
plt.show()
```
