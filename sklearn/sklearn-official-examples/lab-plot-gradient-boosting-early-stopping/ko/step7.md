# 조기 종료 사용 여부에 따른 점수 비교

이제 두 모델의 점수를 비교합니다.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, score_gb, bar_width, label="조기 종료 없음", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, score_gbes, bar_width, label="조기 종료 사용", color="coral"
)

plt.xticks(index + bar_width, names)
plt.yticks(np.arange(0, 1.3, 0.1))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("데이터셋")
plt.ylabel("테스트 점수")

plt.show()
```
