# タイトル、X 軸ラベル、Y 軸ラベルを追加する

`pyplot` ライブラリの `title()`、`xlabel()`、および `ylabel()` メソッドを使って、グラフにタイトル、X 軸ラベル、および Y 軸ラベルを追加することができます。タイトルとして "Voltage vs Time"、X 軸ラベルとして "Time [s]"、Y 軸ラベルとして "Voltage [mV]" を追加します。

```python
plt.title(r'Voltage vs Time', fontsize=20)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
```
