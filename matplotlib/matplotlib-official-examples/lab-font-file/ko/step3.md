# 폰트 경로 설정

`mpl.get_data_path()` 메서드를 사용하여 데이터 디렉토리의 경로를 얻고, `pathlib` 모듈의 `Path()` 메서드를 사용하여 폰트 파일 `cmr10.ttf`의 경로를 추가하여 폰트 경로를 설정합니다.

```python
from pathlib import Path

fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
```
