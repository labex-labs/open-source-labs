# Настройка писателя

Нам нужно настроить писателя, который будет использоваться для записи кадров в файл. Мы задаем количество кадров в секунду (fps) и добавляем метаданные, такие как заголовок, автор и комментарий.

```python
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
```
