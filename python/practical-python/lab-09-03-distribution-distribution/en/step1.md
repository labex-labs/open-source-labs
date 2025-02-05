# Creating a setup.py file

Add a `setup.py` file in `/home/labex/project` directory to the top-level of your project directory.

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
