# 이미지 및 패치 예제 함수 정의

`image_and_patch_example` 함수를 정의합니다. 이 함수는 축 객체를 입력으로 받아 임의의 이미지를 플롯하고 플롯에 패치를 추가합니다.

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```
