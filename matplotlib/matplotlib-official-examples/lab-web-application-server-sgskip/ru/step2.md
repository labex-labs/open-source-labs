# Импорт зависимостей

В этом шаге мы импортируем необходимые зависимости. Мы будем использовать `base64` для кодирования данных изображения, `BytesIO` для хранения данных изображения в памяти, `Flask` для создания сервера веб-приложения и `Figure` для создания графиков.

```python
import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
```
