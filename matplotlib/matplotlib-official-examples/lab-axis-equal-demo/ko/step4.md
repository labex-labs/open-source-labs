# 동일한 축 종횡비를 유지하면서 플롯 제한 조정

또한 동일한 축 종횡비를 유지하면서 플롯 제한을 조정할 수 있습니다.

```python
axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('still a circle, even after changing limits', fontsize=10)
```

결과 플롯은 제한을 변경한 후에도 여전히 비례하는 원을 표시합니다.
