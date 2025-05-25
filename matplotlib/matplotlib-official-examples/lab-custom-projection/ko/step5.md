# 예제 생성

마지막으로, 사용자 정의 투영법을 사용하여 예제를 생성합니다.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # 이제 사용자 정의 투영법을 사용하여 간단한 예제를 만듭니다.
    fig, ax = plt.subplots(subplot_kw={'projection': 'custom_hammer'})
    ax.plot([-1, 1, 1], [-1, -1, 1], "o-")
    ax.grid()

    plt.show()
```
