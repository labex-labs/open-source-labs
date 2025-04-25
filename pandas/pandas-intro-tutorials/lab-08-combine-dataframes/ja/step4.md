# 共通の識別子を使ってテーブルを結合する

次に、`merge`関数を使って、測定値のテーブルに測定所の座標を追加します。`location`列に対して左結合を行います。

```python
# 測定所の座標データを読み込む
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# air_quality と stations_coord のデータフレームを結合する
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```
