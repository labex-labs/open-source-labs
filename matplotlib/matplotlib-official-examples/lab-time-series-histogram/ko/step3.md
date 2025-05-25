# 선 그래프로 데이터 시각화

이 단계에서는 생성된 데이터를 선 그래프로 시각화합니다.

```python
# `plot` 과 작은 `alpha` 값을 사용하여 시계열을 플롯합니다.
# 이 보기에서는 겹치는 시계열이 너무 많아서 사인파 동작을 관찰하기가 매우 어렵습니다.
# 또한 너무 많은 개별 아티스트를 생성해야 하므로 실행하는 데 시간이 약간 걸립니다.
tic = time.time()
plt.plot(x, Y.T, color="C0", alpha=0.1)
toc = time.time()
plt.title("alpha 를 사용한 선 그래프")
plt.show()
print(f"{toc-tic:.3f} sec. elapsed")
```
