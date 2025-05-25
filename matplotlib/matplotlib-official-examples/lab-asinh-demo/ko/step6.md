# 2D 코시 분포 (Cauchy-distributed) 난수에 대한 "symlog" 및 "asinh" 스케일링 비교

마지막으로, 2D 코시 분포 (Cauchy-distributed) 난수에 대한 "symlog" 및 "asinh" 스케일링을 비교해 보겠습니다. 동일한 그래프를 두 번 플롯할 것이며, 한 번은 "symlog"로, 다른 한 번은 "asinh"로 플롯합니다.

```python
fig3 = plt.figure()
ax = fig3.subplots(1, 1)
r = 3 * np.tan(np.random.uniform(-np.pi / 2.02, np.pi / 2.02,
                                 size=(5000,)))
th = np.random.uniform(0, 2*np.pi, size=r.shape)

ax.scatter(r * np.cos(th), r * np.sin(th), s=4, alpha=0.5)
ax.set_xscale('asinh')
ax.set_yscale('symlog')
ax.set_xlabel('asinh')
ax.set_ylabel('symlog')
ax.set_title('2D Cauchy random deviates')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid()
```
