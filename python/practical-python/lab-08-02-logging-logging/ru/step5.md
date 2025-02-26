# Конфигурация журналирования

Поведение журналирования настраивается отдельно.

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # Файл для вывода логов
        level     = logging.INFO,   # Уровень вывода
    )
```

обычно, это一次性配置在程序启动时进行。配置与进行日志记录调用的代码是分开的。 （注：这里“一次性配置”表述不太准确，原文“one-time configuration”更准确意思是“一次性的配置操作”，但按要求尽量贴近原文翻译了）
