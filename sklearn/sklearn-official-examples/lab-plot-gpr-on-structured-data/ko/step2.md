# 시퀀스 유사성 행렬 시각화

`SequenceKernel`을 사용하여 시퀀스 간의 유사성 행렬을 계산할 수 있습니다. 더 밝은 색상이 더 높은 유사성을 나타내는 컬러맵을 사용하여 이 행렬을 플롯합니다.

```python
import matplotlib.pyplot as plt

X = np.array(["AGCT", "AGC", "AACT", "TAA", "AAA", "GAACA"])

kernel = SequenceKernel()
K = kernel(X)
D = kernel.diag(X)

plt.figure(figsize=(8, 5))
plt.imshow(np.diag(D**-0.5).dot(K).dot(np.diag(D**-0.5)))
plt.xticks(np.arange(len(X)), X)
plt.yticks(np.arange(len(X)), X)
plt.title("커널 하의 시퀀스 유사성")
plt.show()
```
