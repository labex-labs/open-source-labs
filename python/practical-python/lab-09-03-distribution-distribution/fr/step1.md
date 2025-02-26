# Création d'un fichier setup.py

Ajoutez un fichier `setup.py` dans le répertoire `/home/labex/project` au niveau supérieur de votre répertoire de projet.

```python
# setup.py
import setuptools

setuptools.setup(
    name="porty",
    version="0.0.1",
    author="Votre nom",
    author_email="vous@exemple.com",
    description="Code Python pratique",
    packages=setuptools.find_packages(),
)
```
