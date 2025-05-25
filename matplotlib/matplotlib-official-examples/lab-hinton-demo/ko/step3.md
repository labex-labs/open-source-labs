# 힌튼 다이어그램 생성

이제 numpy 를 사용하여 무작위 가중치 행렬을 생성한 다음 `hinton` 함수를 사용하여 힌튼 다이어그램을 생성합니다.

```python
if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    hinton(np.random.rand(20, 20) - 0.5)
    plt.show()
```
