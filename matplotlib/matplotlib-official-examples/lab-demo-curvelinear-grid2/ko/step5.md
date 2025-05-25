# Figure 생성

마지막 단계는 `plt.figure` 함수를 사용하여 figure 를 생성하는 것입니다. figure 크기를 (7, 4) 로 설정하고 2-4 단계에서 생성된 `curvelinear_test1` 함수를 호출합니다.

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```
