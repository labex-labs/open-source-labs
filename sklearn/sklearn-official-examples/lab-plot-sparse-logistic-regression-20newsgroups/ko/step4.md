# 결과 시각화

마지막으로 학습된 모델의 결과를 선 그래프를 사용하여 시각화합니다.

```python
fig = plt.figure()
ax = fig.add_subplot(111)

for model in models:
    name = models[model]["name"]
    times = models[model]["times"]
    accuracies = models[model]["accuracies"]
    ax.plot(times, accuracies, marker="o", label="Model: %s" % name)
    ax.set_xlabel("학습 시간 (초)")
    ax.set_ylabel("테스트 정확도")
ax.legend()
fig.suptitle("다항 분류 vs One-vs-Rest 로지스틱 L1 회귀\n데이터셋 %s" % "20newsgroups")
fig.tight_layout()
fig.subplots_adjust(top=0.85)
run_time = timeit.default_timer() - t0
print("예제 실행 시간 %.3f 초" % run_time)
plt.show()
```
