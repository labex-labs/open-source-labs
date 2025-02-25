# Настраиваем метки делений и метки осей для каждой основной трехмерной плоскости обзора

Мы настраиваем метки делений и метки осей для каждой основной трехмерной плоскости обзора, чтобы убрать любые лишние метки.

```python
for plane in ('XY', '-XY'):
    axd[plane].set_zticklabels([])
    axd[plane].set_zlabel('')
for plane in ('XZ', '-XZ'):
    axd[plane].set_yticklabels([])
    axd[plane].set_ylabel('')
for plane in ('YZ', '-YZ'):
    axd[plane].set_xticklabels([])
    axd[plane].set_xlabel('')
```
