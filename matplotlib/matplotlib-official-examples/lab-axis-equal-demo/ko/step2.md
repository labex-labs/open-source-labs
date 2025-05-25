# 불균등한 축 종횡비를 가진 원 그리기

먼저 동일한 축 종횡비를 설정하는 것의 중요성을 보여주기 위해 불균등한 축 종횡비를 가진 원을 그려보겠습니다.

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)
```

결과 플롯은 불균등한 축 종횡비로 인해 길게 보이는 원을 표시합니다.
