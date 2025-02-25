# データセットを連結する

次に、`concat`関数を使って、硝酸塩と微粒子状物質の測定値を1つのテーブルに結合します。

```python
# 2つのデータフレームを連結する
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```
