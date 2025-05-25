# 동일한 축 종횡비를 위한 데이터 제한 자동 조정

`set_aspect('equal', 'box')` 함수를 사용하여 동일한 축 종횡비를 위한 데이터 제한을 자동으로 조정할 수도 있습니다.

```python
axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('still a circle, auto-adjusted data limits', fontsize=10)
```

결과 플롯은 여전히 비례하고 시각적으로 보기 좋은 원을 표시합니다.
