# 線形補間によるデータの補間

2番目のステップは、線形補間法を使ってデータを補間することです。等間隔の四角グリッドを作成し、その後、LinearTriInterpolatorメソッドを使ってデータを補間します。最後に、補間されたデータをプロットします。

```python
# Interpolate to regularly-spaced quad grid.
z = np.cos(1.5 * x) * np.cos(1.5 * y)
xi, yi = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 3, 20))

# Interpolate using linear method.
interp_lin = mtri.LinearTriInterpolator(triang, z)
zi_lin = interp_lin(xi, yi)

# Plot the interpolated data.
plt.contourf(xi, yi, zi_lin)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Linear interpolation")
plt.show()
```
