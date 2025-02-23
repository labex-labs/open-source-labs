# 2次元コーシー分布乱数における「symlog」と「asinh」のスケーリングを比較する

最後に、2次元コーシー分布乱数における「symlog」と「asinh」のスケーリングを比較します。同じグラフを2回プロットします。1回は「symlog」で、もう1回は「asinh」でプロットします。

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
