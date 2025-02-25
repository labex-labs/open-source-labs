# Задаем путь к шрифту

Мы задаем путь к шрифту с помощью метода `mpl.get_data_path()` для получения пути к директории с данными, а затем добавляем к нему путь к файлу шрифта `cmr10.ttf` с использованием метода `Path()` из модуля `pathlib`.

```python
from pathlib import Path

fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
```
