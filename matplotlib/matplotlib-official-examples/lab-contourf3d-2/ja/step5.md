# 等高線プロファイルを投影する

次に、グラフの壁に等高線プロファイルを投影します。これは `contourf` メソッドを使用して行われます。等高線プロファイルをそれぞれ z、x、y の壁に投影するには、`zdir` パラメータを 'z'、'x'、'y' に設定します。また、適切な軸の範囲に一致するように `offset` パラメータを設定します。

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
