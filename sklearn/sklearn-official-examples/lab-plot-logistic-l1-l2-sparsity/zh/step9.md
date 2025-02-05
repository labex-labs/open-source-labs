# 打印结果

我们将打印每个模型的稀疏性和分数。

```python
    print("C=%.2f" % C)
    print("{:<40} {:.2f}%".format("L1 惩罚的稀疏性:", sparsity_l1_LR))
    print("{:<40} {:.2f}%".format("弹性网络惩罚的稀疏性:", sparsity_en_LR))
    print("{:<40} {:.2f}%".format("L2 惩罚的稀疏性:", sparsity_l2_LR))
    print("{:<40} {:.2f}".format("L1 惩罚的分数:", score_l1_LR))
    print("{:<40} {:.2f}".format("弹性网络惩罚的分数:", score_en_LR))
    print("{:<40} {:.2f}".format("L2 惩罚的分数:", score_l2_LR))
```
