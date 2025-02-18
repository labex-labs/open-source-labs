# 目盛りパラメータをカスタマイズする

グラフの外観をさらに調整するために、目盛りパラメータをカスタマイズすることもできます。この例では、目盛りラベルの色を緑に変更し、グラフの右側に移動させます。

```python
# Customize tick parameters
ax.tick_params(axis='y', which='major', labelcolor='green', labelright=True)
```

上記のコードでは、`tick_params` メソッドを使用して y 軸の目盛りパラメータをカスタマイズしています。`axis` パラメータを `'y'` に設定して y 軸をカスタマイズすることを指定し、`which` パラメータを `'major'` に設定して主目盛りをカスタマイズすることを指定しています。`labelcolor` パラメータを `'green'` に設定して目盛りラベルの色を変更し、`labelright` パラメータを `True` に設定して目盛りラベルをグラフの右側に移動させています。
