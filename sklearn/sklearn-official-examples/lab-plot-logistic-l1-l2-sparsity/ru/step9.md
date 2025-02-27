# Выводим результаты

Мы выведем разреженность и оценки для каждой модели.

```python
    print("C=%.2f" % C)
    print("{:<40} {:.2f}%".format("Sparsity with L1 penalty:", sparsity_l1_LR))
    print("{:<40} {:.2f}%".format("Sparsity with Elastic-Net penalty:", sparsity_en_LR))
    print("{:<40} {:.2f}%".format("Sparsity with L2 penalty:", sparsity_l2_LR))
    print("{:<40} {:.2f}".format("Score with L1 penalty:", score_l1_LR))
    print("{:<40} {:.2f}".format("Score with Elastic-Net penalty:", score_en_LR))
    print("{:<40} {:.2f}".format("Score with L2 penalty:", score_l2_LR))
```
