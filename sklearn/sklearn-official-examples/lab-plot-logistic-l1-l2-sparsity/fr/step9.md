# Afficher les résultats

Nous allons afficher la rareté et les scores pour chaque modèle.

```python
    print("C=%.2f" % C)
    print("{:<40} {:.2f}%".format("Rareté avec la pénalité L1 :", sparsity_l1_LR))
    print("{:<40} {:.2f}%".format("Rareté avec la pénalité Elastic-Net :", sparsity_en_LR))
    print("{:<40} {:.2f}%".format("Rareté avec la pénalité L2 :", sparsity_l2_LR))
    print("{:<40} {:.2f}".format("Score avec la pénalité L1 :", score_l1_LR))
    print("{:<40} {:.2f}".format("Score avec la pénalité Elastic-Net :", score_en_LR))
    print("{:<40} {:.2f}".format("Score avec la pénalité L2 :", score_l2_LR))
```
