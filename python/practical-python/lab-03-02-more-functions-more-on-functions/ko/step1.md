# 함수 호출 (Calling a Function)

다음 함수를 고려해 봅시다:

```python
def read_prices(filename, debug):
    ...
```

위 함수는 위치 인자 (positional arguments) 를 사용하여 호출할 수 있습니다:

    prices = read_prices('prices.csv', True)

또는 키워드 인자 (keyword arguments) 를 사용하여 함수를 호출할 수 있습니다:

```python
prices = read_prices(filename='prices.csv', debug=True)
```
