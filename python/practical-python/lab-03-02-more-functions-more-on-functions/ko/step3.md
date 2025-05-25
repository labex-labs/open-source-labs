# 선택적 인자에 키워드 인자 사용 권장 (Prefer keyword arguments for optional arguments)

다음 두 가지 호출 스타일을 비교해 봅시다:

```python
parse_data(data, False, True) # ?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

대부분의 경우, 키워드 인자는 코드의 명확성을 향상시킵니다. 특히 플래그 (flags) 역할을 하거나 선택적 기능과 관련된 인자의 경우 더욱 그렇습니다.
