# Optionen zurücksetzen

Wenn wir eine oder mehrere Optionen auf ihren Standardwert zurücksetzen möchten, können wir `pd.reset_option` verwenden.

```python
# Reset the maximum display rows to default
pd.reset_option("display.max_rows")

# Verify the reset
print(pd.options.display.max_rows)
```
