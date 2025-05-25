# 출력 (Printing)

`print` 함수는 전달된 값으로 단일 텍스트 줄을 생성합니다.

```python
print('Hello world!') # Prints the text 'Hello world!'
```

변수를 사용할 수 있습니다. 출력되는 텍스트는 변수의 이름이 아닌 변수의 값입니다.

```python
x = 100
print(x) # Prints the text '100'
```

`print`에 둘 이상의 값을 전달하면 공백으로 구분됩니다.

```python
name = 'Jake'
print('My name is', name) # Print the text 'My name is Jake'
```

`print()`는 항상 끝에 줄 바꿈 문자를 추가합니다.

```python
print('Hello')
print('My name is', 'Jake')
```

이것은 다음을 출력합니다:

```code
Hello
My name is Jake
```

추가적인 줄 바꿈은 억제될 수 있습니다:

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

이 코드는 이제 다음을 출력합니다:

```code
Hello My name is Jake
```
