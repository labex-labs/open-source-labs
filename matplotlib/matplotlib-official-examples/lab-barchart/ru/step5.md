# Настраиваем график

Мы можем настроить график, добавив подписи, заголовок и настроив метки делений оси x и легенду. Также мы установим предел оси y, чтобы убедиться, что все наши данные видны.

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```
