# 옵션 가져오기 및 설정하기

`pd.get_option` 또는 `pd.set_option`을 사용하여 단일 옵션의 값을 가져오거나 설정할 수 있습니다. 여기서는 최대 표시 행을 999 로 설정합니다.

```python
# Get the current setting for maximum display rows
print(pd.options.display.max_rows)

# Set the maximum display rows to 999
pd.options.display.max_rows = 999

# Verify the new setting
print(pd.options.display.max_rows)
```
