# Erstellen einer setup.py-Datei

Fügen Sie eine `setup.py`-Datei im Verzeichnis `/home/labex/project` in das oberste Verzeichnis Ihres Projekts hinzu.

```python
# setup.py
import setuptools

setuptools.setup(
    name="porty",
    version="0.0.1",
    author="Ihr Name",
    author_email="you@example.com",
    description="Praktischer Python-Code",
    packages=setuptools.find_packages(),
)
```
