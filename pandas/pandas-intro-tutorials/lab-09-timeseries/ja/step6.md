# 時系列データをリサンプリングする

`resample` メソッドは、時系列データの頻度を変更する強力な方法です。ここでは、現在の毎時の時系列データを各測定地点で月間最大値に集約します。

```python
# データをピボットすることで、日付時刻情報が表のインデックスになりました。
no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
no_2.head()

# 5月20日から5月21日の終わりまでの異なる測定地点の値のプロットを作成する
no_2["2019-05-20":"2019-05-21"].plot()

# 時系列データをリサンプリングする
monthly_max = no_2.resample("M").max()
monthly_max
```
