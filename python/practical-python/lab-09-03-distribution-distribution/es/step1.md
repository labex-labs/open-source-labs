# Creando un archivo setup.py

Agrega un archivo `setup.py` en el directorio `/home/labex/project` al nivel superior de tu directorio de proyecto.

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
