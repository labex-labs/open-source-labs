# 데이터 플롯

이제 `plot` 함수를 사용하여 데이터를 플롯할 수 있습니다. 3 단계에서 생성한 데이터를 사용하여 두 개의 선을 생성합니다.

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```
