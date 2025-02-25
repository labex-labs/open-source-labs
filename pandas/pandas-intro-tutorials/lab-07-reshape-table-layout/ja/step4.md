# ピボットテーブルを作成する

各測定所における 𝑁𝑂2 と 𝑃𝑀25 の平均濃度を求めるために、ピボットテーブルを作成します。

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```
