# Imprimir los resultados

Imprimiremos la esparsidad y las puntuaciones para cada modelo.

```python
    print("C=%.2f" % C)
    print("{:<40} {:.2f}%".format("Eparsidad con penalización L1:", sparsity_l1_LR))
    print("{:<40} {:.2f}%".format("Eparsidad con penalización Elastic-Net:", sparsity_en_LR))
    print("{:<40} {:.2f}%".format("Eparsidad con penalización L2:", sparsity_l2_LR))
    print("{:<40} {:.2f}".format("Puntuación con penalización L1:", score_l1_LR))
    print("{:<40} {:.2f}".format("Puntuación con penalización Elastic-Net:", score_en_LR))
    print("{:<40} {:.2f}".format("Puntuación con penalización L2:", score_l2_LR))
```
