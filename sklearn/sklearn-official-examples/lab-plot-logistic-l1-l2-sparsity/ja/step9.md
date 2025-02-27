# 結果を表示する

各モデルの疎密度とスコアを表示します。

```python
    print("C=%.2f" % C)
    print("{:<40} {:.2f}%".format("L1ペナルティによる疎密度:", sparsity_l1_LR))
    print("{:<40} {:.2f}%".format("エラスティックネットペナルティによる疎密度:", sparsity_en_LR))
    print("{:<40} {:.2f}%".format("L2ペナルティによる疎密度:", sparsity_l2_LR))
    print("{:<40} {:.2f}".format("L1ペナルティによるスコア:", score_l1_LR))
    print("{:<40} {:.2f}".format("エラスティックネットペナルティによるスコア:", score_en_LR))
    print("{:<40} {:.2f}".format("L2ペナルティによるスコア:", score_l2_LR))
```
