# Зададим основные и вторичные делители

```python
# Set the major locator
ax.xaxis.set_major_locator(MultipleLocator(20))
# Set the major formatter
ax.xaxis.set_major_formatter('{x:.0f}')
# Set the minor locator
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

Здесь мы задаем основные делители, чтобы деления шкалы располагались через каждые 20 единиц, задаем форматтер для основных делений, чтобы эти деления были помечены с использованием формата ".0f", и задаем вторичные делители, чтобы деления шкалы располагались через каждые 5 единиц.
