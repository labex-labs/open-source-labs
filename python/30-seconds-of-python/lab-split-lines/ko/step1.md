# 줄로 분할하기

`split_lines(s)`라는 함수를 작성하세요. 이 함수는 여러 줄 문자열 `s`를 입력으로 받아 개별 줄의 목록을 반환합니다. 함수는 각 줄 바꿈 문자 (`\n`) 에서 문자열을 분할하고 결과 줄의 목록을 반환해야 합니다.

```python
def split_lines(s):
  return s.split('\n')
```

```python
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a', 'multiline', 'string.' , '']
```
