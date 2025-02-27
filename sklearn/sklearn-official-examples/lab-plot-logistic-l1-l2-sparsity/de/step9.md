# Ergebnisse ausgeben

Wir werden die Sparsität und die Scores für jedes Modell ausgeben.

```python
    print("C=%.2f" % C)
    print("{:<40} {:.2f}%".format("Sparsität mit L1-Strafe:", sparsity_l1_LR))
    print("{:<40} {:.2f}%".format("Sparsität mit Elastic-Net-Strafe:", sparsity_en_LR))
    print("{:<40} {:.2f}%".format("Sparsität mit L2-Strafe:", sparsity_l2_LR))
    print("{:<40} {:.2f}".format("Score mit L1-Strafe:", score_l1_LR))
    print("{:<40} {:.2f}".format("Score mit Elastic-Net-Strafe:", score_en_LR))
    print("{:<40} {:.2f}".format("Score mit L2-Strafe:", score_l2_LR))
```
