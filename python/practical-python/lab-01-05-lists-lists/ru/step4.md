# Удаление элементов из списка

Вы можете удалять элементы списка либо по значению, либо по индексу:

```python
# Используя значение
names.remove('Curtis')

# Используя индекс
del names[1]
```

При удалении элемента не создается пропуск. Другие элементы сдвигаются вниз, чтобы заполнить освободившееся место. Если элемент встречается более одного раза, `remove()` удалит только первое вхождение.
