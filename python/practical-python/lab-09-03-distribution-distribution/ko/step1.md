# setup.py 파일 생성

`/home/labex/project` 디렉토리의 프로젝트 최상위 레벨에 `setup.py` 파일을 추가합니다.

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
