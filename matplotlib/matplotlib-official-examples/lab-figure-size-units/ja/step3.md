# センチメートル単位のグラフサイズ

グラフサイズをセンチメートル単位で指定することもできます。このためには、センチメートル単位の数値をインチに変換する必要があります。これは、センチメートル値に cm からインチへの変換係数である 1/2.54 を掛けることで行えます。その後、この値をサブプロット関数の figsize パラメータとして使用できます。以下のコードは、15cm×5cm のサイズのグラフを作成する方法を示しています。

```python
cm = 1/2.54  # インチにおけるセンチメートル
plt.subplots(figsize=(15*cm, 5*cm))
plt.show()
```
