# 결과 플롯

이제 각 특징과 각 특징에 대한 F-검정 및 상호 정보량 점수에 대한 대상의 종속성을 플롯합니다.

```python
plt.figure(figsize=(15, 5))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.scatter(X[:, i], y, edgecolor="black", s=20)
    plt.xlabel("$x_{}$".format(i + 1), fontsize=14)
    if i == 0:
        plt.ylabel("$y$", fontsize=14)
    plt.title("F-검정={:.2f}, 상호 정보량={:.2f}".format(f_test[i], mi[i]), fontsize=16)
plt.show()
```
