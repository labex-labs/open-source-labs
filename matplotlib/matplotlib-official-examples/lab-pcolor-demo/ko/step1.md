# 간단한 Pcolor 데모

첫 번째 단계는 간단한 Pcolor 데모를 만드는 것입니다. 이것은 기본적인 Pcolor 플롯을 생성하는 방법을 보여줍니다.

```python
Z = np.random.rand(6, 10)

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(Z)
ax0.set_title('default: no edges')

c = ax1.pcolor(Z, edgecolors='k', linewidths=4)
ax1.set_title('thick edges')

fig.tight_layout()
plt.show()
```
