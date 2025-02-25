# Рисуем тексты на фигуре с позиционированием в пиксельных координатах

Вместо этого мы можем напрямую нарисовать текст на фигуре с позиционированием в пиксельных координатах, используя `.Figure.text` вместе с `.transforms.IdentityTransform`.

```python
fig.text(100, 250, r"IQ: $\sigma_i=15$", color="blue", fontsize=20, transform=IdentityTransform())
fig.text(100, 350, r"some other string", color="red", fontsize=20, transform=IdentityTransform())

plt.show()
```
