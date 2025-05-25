# option_context 사용하기

`option_context` 함수를 사용하면 실행 후 이전 설정으로 되돌아가는 옵션 집합으로 코드 블록을 실행할 수 있습니다.

```python
# Execute a code block with a set of options
with pd.option_context("display.max_rows", 10):
    # This will print 10 despite the global setting being different
    print(pd.get_option("display.max_rows"))

# This will print the global setting as the context block has ended
print(pd.get_option("display.max_rows"))
```
