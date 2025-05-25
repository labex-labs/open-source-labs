# 플롯 생성

이제 `LassoManager` 클래스를 사용하여 대화형 플롯을 생성합니다. `np.random.rand` 함수는 플롯될 임의의 데이터 포인트를 생성합니다.

```python
if __name__ == '__main__':
    np.random.seed(19680801)
    ax = plt.figure().add_subplot(
        xlim=(0, 1), ylim=(0, 1), title='Lasso points using left mouse button')
    manager = LassoManager(ax, np.random.rand(100, 2))
    plt.show()
```
