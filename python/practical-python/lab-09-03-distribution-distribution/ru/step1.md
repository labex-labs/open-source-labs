# Создание файла setup.py

Добавьте файл `setup.py` в директорию `/home/labex/project` в верхний уровень вашего каталога проекта.

```python
# setup.py
import setuptools

setuptools.setup(
    name="porty",
    version="0.0.1",
    author="Your Name",
    author_email="you@example.com",
    description="Practical Python Code",
    packages=setuptools.find_packages(),
)
```
