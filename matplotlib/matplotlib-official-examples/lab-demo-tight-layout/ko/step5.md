# 플롯 저장

플롯을 생성한 후에는 파일을 저장할 수 있습니다.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.savefig('my_plot.png')
```

여기서는 `savefig` 함수를 사용하여 플롯을 `my_plot.png`라는 파일로 저장합니다.
