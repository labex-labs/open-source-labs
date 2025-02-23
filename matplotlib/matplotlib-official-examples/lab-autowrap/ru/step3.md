# Автоматическое перенос текста

Теперь давайте изучим, как автоматически переносить текст в Matplotlib. Замените строку `plt.text()` в своем коде на следующую:

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

Аргумент `wrap=True` сообщает Matplotlib автоматически переносить текст.
