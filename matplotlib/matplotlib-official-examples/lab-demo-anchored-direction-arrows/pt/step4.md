# Criar uma seta de alto contraste

Em seguida, criaremos uma seta direcional ancorada de alto contraste. Esta seta terá um contorno branco e um preenchimento preto.

```python
high_contrast_part_1 = AnchoredDirectionArrows(
                            ax.transAxes,
                            '111', r'11$\overline{2}$',
                            loc='upper right',
                            arrow_props={'ec': 'w', 'fc': 'none', 'alpha': 1,
                                         'lw': 2}
                            )
ax.add_artist(high_contrast_part_1)

high_contrast_part_2 = AnchoredDirectionArrows(
                            ax.transAxes,
                            '111', r'11$\overline{2}$',
                            loc='upper right',
                            arrow_props={'ec': 'none', 'fc': 'k'},
                            text_props={'ec': 'w', 'fc': 'k', 'lw': 0.4}
                            )
ax.add_artist(high_contrast_part_2)
```
