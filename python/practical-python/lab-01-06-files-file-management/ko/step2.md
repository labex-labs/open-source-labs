# 파일 데이터 읽기를 위한 일반적인 관용구 (Common Idioms for Reading File Data)

전체 파일을 한 번에 문자열로 읽습니다.

```python
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` 는 `foo.txt` 의 모든 텍스트가 포함된 문자열입니다.
```

반복하여 파일을 줄 단위로 읽습니다.

```python
with open(filename, 'rt') as file:
    for line in file:
        # 라인 처리
```
