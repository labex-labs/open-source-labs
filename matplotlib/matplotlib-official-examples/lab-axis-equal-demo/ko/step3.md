# 동일한 축 종횡비를 가진 원 그리기

동일한 축 종횡비를 설정하기 위해 `axis('equal')` 함수를 사용할 수 있습니다.

```python
axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('equal, looks like circle', fontsize=10)
```

결과 플롯은 비례하고 시각적으로 보기 좋은 원을 표시합니다.
