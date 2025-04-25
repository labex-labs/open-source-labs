# 寄生虫軸を作成する

`host.get_aux_axes()`メソッドを使って 2 つの寄生虫軸を作成します。`viewlim_mode=None`を設定して、寄生虫軸がホスト軸と同じ x スケールを共有することを確認します。また、`sharex=host`を設定して、x スケールが共有されることを確認します。

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```
