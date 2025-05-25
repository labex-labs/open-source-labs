# 파일 입출력 (File Input and Output)

파일을 엽니다.

```python
f = open('foo.txt', 'rt')     # 읽기 (텍스트) 용으로 열기
g = open('bar.txt', 'wt')     # 쓰기 (텍스트) 용으로 열기
```

모든 데이터를 읽습니다.

```python
data = f.read()

# 'maxbytes' 바이트까지만 읽기
data = f.read([maxbytes])
```

일부 텍스트를 씁니다.

```python
g.write('some text')
```

작업이 끝나면 닫습니다.

```python
f.close()
g.close()
```

파일은 적절하게 닫혀야 하며, 잊기 쉬운 단계입니다. 따라서 선호되는 접근 방식은 다음과 같이 `with` 문을 사용하는 것입니다.

```python
with open(filename, 'rt') as file:
    # 파일 `file` 사용
    ...
    # 명시적으로 닫을 필요 없음
...statements
```

이렇게 하면 들여쓰기된 코드 블록에서 제어가 벗어날 때 파일이 자동으로 닫힙니다.
