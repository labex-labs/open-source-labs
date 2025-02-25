# StepPatch アーティストを作成する

```python
patch = StepPatch(values=[1, 2, 3, 2, 1],
                  edges=range(1, 7),
                  label=('Patch derived underlying object\n'
                         'with default edge/facecolor behaviour'))
plt.gca().add_patch(patch)
plt.xlim(0, 7)
plt.ylim(-1, 5)
plt.legend()
plt.show()
```
