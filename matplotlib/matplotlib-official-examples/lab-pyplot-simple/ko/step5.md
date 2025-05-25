# 플롯 저장

`savefig` 메서드를 사용하여 플롯을 이미지 파일로 저장할 수 있습니다. 다음 코드는 플롯을 PNG 이미지로 저장합니다.

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.savefig('simple_plot.png')
```
