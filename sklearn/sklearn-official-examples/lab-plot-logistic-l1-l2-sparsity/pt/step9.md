# Imprimir Resultados

Imprimiremos a esparcidade e as pontuações para cada modelo.

```python
    print("C=%.2f" % C)
    print("{:<40} {:.2f}%".format("Esparsidade com penalidade L1:", sparsity_l1_LR))
    print("{:<40} {:.2f}%".format("Esparsidade com penalidade Rede elástica:", sparsity_en_LR))
    print("{:<40} {:.2f}%".format("Esparsidade com penalidade L2:", sparsity_l2_LR))
    print("{:<40} {:.2f}".format("Pontuação com penalidade L1:", score_l1_LR))
    print("{:<40} {:.2f}".format("Pontuação com penalidade Rede elástica:", score_en_LR))
    print("{:<40} {:.2f}".format("Pontuação com penalidade L2:", score_l2_LR))
```
