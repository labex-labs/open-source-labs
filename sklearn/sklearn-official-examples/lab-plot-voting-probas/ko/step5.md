# 클래스 확률 시각화

각 분류기와 VotingClassifier 의 클래스 확률을 막대 그래프로 시각화합니다.

```python
N = 4  # 그룹 수
ind = np.arange(N)  # 그룹 위치
width = 0.35  # 막대 너비

fig, ax = plt.subplots()

# 분류기 1-3 에 대한 막대
p1 = ax.bar(ind, np.hstack(([class1_1[:-1], [0]])), width, color="green", edgecolor="k")
p2 = ax.bar(
    ind + width,
    np.hstack(([class2_1[:-1], [0]])),
    width,
    color="lightgreen",
    edgecolor="k",
)

# VotingClassifier 에 대한 막대
p3 = ax.bar(ind, [0, 0, 0, class1_1[-1]], width, color="blue", edgecolor="k")
p4 = ax.bar(
    ind + width, [0, 0, 0, class2_1[-1]], width, color="steelblue", edgecolor="k"
)

# 플롯 주석
plt.axvline(2.8, color="k", linestyle="dashed")
ax.set_xticks(ind + width)
ax.set_xticklabels(
    [
        "LogisticRegression\n가중치 1",
        "GaussianNB\n가중치 1",
        "RandomForestClassifier\n가중치 5",
        "VotingClassifier\n(평균 확률)",
    ],
    rotation=40,
    ha="right",
)
plt.ylim([0, 1])
plt.title("다양한 분류기의 샘플 1 에 대한 클래스 확률")
plt.legend([p1[0], p2[0]], ["클래스 1", "클래스 2"], loc="upper left")
plt.tight_layout()
plt.show()
```
