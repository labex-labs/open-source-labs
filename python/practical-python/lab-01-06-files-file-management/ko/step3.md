# 파일에 쓰기를 위한 일반적인 관용구 (Common Idioms for Writing to a File)

문자열 데이터를 씁니다.

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
    ...
```

print 함수를 리디렉션합니다.

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
    ...
```

이 연습은 `portfolio.csv` 파일에 의존합니다. 이 파일에는 주식 포트폴리오에 대한 정보가 포함된 줄 목록이 있습니다. `~/project/` 디렉토리에서 작업한다고 가정합니다. 확실하지 않은 경우, Python 이 실행 중이라고 생각하는 위치를 다음과 같이 확인할 수 있습니다.

```python
>>> import os
>>> os.getcwd()
'/home/labex/project' # 출력은 다를 수 있습니다.
>>>
```
