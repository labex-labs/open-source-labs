# 조기 종료 사용 여부에 따른 학습 시간 비교

이제 두 모델의 학습 시간을 비교합니다.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, time_gb, bar_width, label="조기 종료 없음", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, time_gbes, bar_width, label="조기 종료 사용", color="coral"
)

max_y = np.amax(np.maximum(time_gb, time_gbes))

plt.xticks(index + bar_width, names)
plt.yticks(np.linspace(0, 1.3 * max_y, 13))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3 * max_y])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("데이터셋")
plt.ylabel("학습 시간")

plt.show()
```
