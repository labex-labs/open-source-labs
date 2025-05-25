# Criando um arquivo setup.py

Adicione um arquivo `setup.py` no diretório `/home/labex/project` ao nível superior do diretório do seu projeto.

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
