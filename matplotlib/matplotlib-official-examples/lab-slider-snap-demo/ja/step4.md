# 振幅スライダーの許可値を定義する

このステップでは、振幅スライダーの許可値を定義します。振幅スライダーはこれらの値を使って最も近い許可値にスナップします。

```python
# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])
```
