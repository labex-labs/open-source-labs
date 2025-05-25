# 애니메이션 생성

for 루프를 사용하여 애니메이션의 각 프레임을 반복합니다. 각 반복에서 축을 지우고, 현재 프레임을 플롯하고, 제목을 설정하고, 애니메이션이 표시되도록 짧은 시간 동안 일시 중지합니다.

```python
fig, ax = plt.subplots()

for i, img in enumerate(data):
    ax.clear()
    ax.imshow(img)
    ax.set_title(f"frame {i}")
    plt.pause(0.1)
```
