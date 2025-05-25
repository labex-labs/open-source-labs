# 바이트 문자열 (Byte Strings)

일반적으로 저수준 I/O 에서 사용되는 8 비트 바이트 문자열은 다음과 같이 작성됩니다.

```python
data = b'Hello World\r\n'
```

첫 번째 따옴표 앞에 작은 `b`를 붙여서 텍스트 문자열이 아닌 바이트 문자열임을 지정합니다.

대부분의 일반적인 문자열 연산이 작동합니다.

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

인덱싱은 바이트 값을 정수로 반환하기 때문에 약간 다릅니다.

```python
data[0]   # 72 (ASCII code for 'H')
```

텍스트 문자열로/에서 변환.

```python
text = data.decode('utf-8') # bytes -> text
data = text.encode('utf-8') # text -> bytes
```

`'utf-8'` 인수는 문자 인코딩을 지정합니다. 다른 일반적인 값으로는 `'ascii'` 및 `'latin1'`이 있습니다.
