# 이름, 값, 타입 (Names, Values, Types)

변수 이름은 *타입*을 가지지 않습니다. 그것은 단지 이름일 뿐입니다. 하지만, 값은 근본적인 타입을 _가지고_ 있습니다.

```python
>>> a = 42
>>> b = 'Hello World'
>>> type(a)
<type 'int'>
>>> type(b)
<type 'str'>
```

`type()`은 그것이 무엇인지 알려줍니다. 타입 이름은 일반적으로 값을 해당 타입으로 생성하거나 변환하는 함수로 사용됩니다.
