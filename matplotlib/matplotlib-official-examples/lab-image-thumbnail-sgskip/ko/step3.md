# 인수 파싱 (Parse Arguments)

이 단계에서는 프로그램에 전달된 인수를 파싱합니다. `ArgumentParser` 객체를 생성하고 `imagedir`라는 인수를 추가해야 합니다. 이 인수는 이미지가 포함된 디렉토리의 경로를 지정합니다. `type` 매개변수를 사용하여 인수의 데이터 유형을 지정할 수 있습니다. 이 경우 인수는 `Path` 유형이어야 합니다.

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```
