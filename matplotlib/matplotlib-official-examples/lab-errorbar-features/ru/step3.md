# Определяем значения ошибок

Теперь мы определим наши значения ошибок. В этом примере мы будем использовать переменную `error` для представления симметричной ошибки и переменную `asymmetric_error` для представления асимметричной ошибки.

```python
# example error bar values that vary with x-position
error = 0.1 + 0.2 * x

# error bar values w/ different -/+ errors that
# also vary with the x-position
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
```
