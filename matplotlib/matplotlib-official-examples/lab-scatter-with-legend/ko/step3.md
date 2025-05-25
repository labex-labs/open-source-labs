# 자동 범례 생성

`PathCollection.legend_elements` 메서드를 사용하여 산점도에 대한 범례를 자동으로 생성할 수도 있습니다. 이 메서드는 표시할 유용한 수의 범례 항목을 결정하려고 시도하고 핸들과 레이블의 튜플을 반환합니다.

```python
N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 220, size=N)

fig, ax = plt.subplots()

scatter = ax.scatter(x, y, c=c, s=s)

# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
ax.add_artist(legend1)

# produce a legend with a cross-section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

plt.show()
```
