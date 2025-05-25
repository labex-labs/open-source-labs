# 데이터셋 시각화

생성된 클러스터를 시각화하여 데이터셋의 모습을 확인할 수 있습니다.

```python
import matplotlib.pyplot as plt

scatter = plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
handles, labels = scatter.legend_elements()
plt.axis("square")
plt.legend(handles=handles, labels=["이상치", "내부 데이터 포인트"], title="실제 클래스")
plt.title("가우시안 내부 데이터 포인트와 \n균일 분포된 이상치")
plt.show()
```
