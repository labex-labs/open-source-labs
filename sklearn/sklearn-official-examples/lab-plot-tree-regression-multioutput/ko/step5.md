# 결과 플롯

이 단계에서는 결과를 플롯합니다. `matplotlib.pyplot`를 사용하여 원본 데이터의 산점도와 세 가지 모델 예측 각각을 그립니다. 또한 플롯에 레이블과 제목을 추가합니다.

```python
# 결과 플롯
plt.figure()
s = 25
plt.scatter(y[:, 0], y[:, 1], c="navy", s=s, edgecolor="black", label="data")
plt.scatter(
    y_1[:, 0],
    y_1[:, 1],
    c="cornflowerblue",
    s=s,
    edgecolor="black",
    label="max_depth=2",
)
plt.scatter(y_2[:, 0], y_2[:, 1], c="red", s=s, edgecolor="black", label="max_depth=5")
plt.scatter(
    y_3[:, 0], y_3[:, 1], c="orange", s=s, edgecolor="black", label="max_depth=8"
)
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.xlabel("target 1")
plt.ylabel("target 2")
plt.title("다중 출력 결정 트리 회귀")
plt.legend(loc="best")
plt.show()
```
