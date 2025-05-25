# 여러 개의 범례 키를 가진 범례 항목 생성

이 단계에서는 여러 개의 범례 키를 가진 범례 항목을 생성합니다.

```python
# Define data for the chart
fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
p1 = ax1.scatter([1], [5], c='r', marker='s', s=100)
p2 = ax1.scatter([3], [2], c='b', marker='o', s=100)
p3, = ax1.plot([1, 5], [4, 4], 'm-d')

# Create a legend with two keys for one entry
l = ax1.legend([(p1, p3), p2], ['two keys', 'one key'], scatterpoints=1,
               numpoints=1, handler_map={tuple: HandlerTuple(ndivide=None)})

# Create two bar charts on top of each other and change the padding between the legend keys
x_left = [1, 2, 3]
y_pos = [1, 3, 2]
y_neg = [2, 1, 4]
rneg = ax2.bar(x_left, y_neg, width=0.5, color='w', hatch='///', label='-1')
rpos = ax2.bar(x_left, y_pos, width=0.5, color='k', label='+1')

# Treat each legend entry differently by using specific `HandlerTuple`s
l = ax2.legend([(rpos, rneg), (rneg, rpos)], ['pad!=0', 'pad=0'],
               handler_map={(rpos, rneg): HandlerTuple(ndivide=None),
                            (rneg, rpos): HandlerTuple(ndivide=None, pad=0.)})

# Display the chart
plt.show()
```
