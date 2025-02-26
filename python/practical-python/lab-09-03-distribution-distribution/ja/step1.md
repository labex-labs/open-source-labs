# setup.py ファイルの作成

プロジェクトディレクトリのトップレベルに、`/home/labex/project` ディレクトリに `setup.py` ファイルを追加します。

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
