# Auto Shading (자동 쉐이딩)

사용자가 코드가 자동으로 사용할 쉐이딩을 선택하도록 하려는 경우, `shading='auto'`는 `X`, `Y`, 그리고 `Z`의 형태를 기반으로 `flat` 또는 `nearest` 쉐이딩을 사용할지 결정합니다. 다음 코드 블록을 사용하여 그리드를 시각화할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, shading='auto', cmap='viridis')
ax.set_title('Auto Shading')
plt.show()
```
