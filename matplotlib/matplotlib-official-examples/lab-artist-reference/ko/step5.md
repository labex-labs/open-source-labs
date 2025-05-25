# 플롯 저장

`savefig` 함수를 사용하여 플롯을 이미지 파일로 저장할 수 있습니다.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.savefig('shapes.png')
```
