# 誤差値の定義

次に、誤差値を定義します。この例では、対称誤差を表すために`error`変数を、非対称誤差を表すために`asymmetric_error`変数を使用します。

```python
# example error bar values that vary with x-position
error = 0.1 + 0.2 * x

# error bar values w/ different -/+ errors that
# also vary with the x-position
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
```
