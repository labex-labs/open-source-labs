# 옵션 재설정하기

하나 이상의 옵션을 기본값으로 재설정하려면 `pd.reset_option`을 사용할 수 있습니다.

```python
# Reset the maximum display rows to default
pd.reset_option("display.max_rows")

# Verify the reset
print(pd.options.display.max_rows)
```
