# Добавляем текст на график

Мы можем добавить текст на наш график с использованием функции text(). В этом примере мы добавим LaTeX-выражение на график, используя словарь шрифта для настройки стиля.

```python
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
```
