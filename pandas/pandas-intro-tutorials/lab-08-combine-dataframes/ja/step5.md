# パラメータの完全な説明と名前を追加する

最後に、測定値のテーブルにパラメータの完全な説明と名前を追加します。`parameter`列と`id`列に対して左結合を行います。

```python
# 空気質パラメータのデータを読み込む
air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv")

# air_qualityとair_quality_parametersのデータフレームを結合する
air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
```
