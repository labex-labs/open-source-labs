# `.Line2D.set_dashes()` を使って破線シーケンスを変更する

`.Line2D.set_dashes()` を使って破線シーケンスを変更することができます。この例では、`line1` の破線シーケンスを変更して、2pt の線、2pt の間隔、10pt の線、2pt の間隔の破線パターンを作成します。また、`line1.set_dash_capstyle()` を使ってキャップスタイルを 'round' に設定します。

```python
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break.
line1.set_dash_capstyle('round')
```
