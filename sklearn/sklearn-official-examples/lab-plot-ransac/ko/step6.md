# 결과 시각화

선형 모델과 RANSAC 회귀 분석기의 데이터와 적합된 직선을 플롯합니다.

```python
# 결과 시각화
lw = 2
plt.scatter(
    X[inlier_mask], y[inlier_mask], color="yellowgreen", marker=".", label="내재값"
)
plt.scatter(
    X[outlier_mask], y[outlier_mask], color="gold", marker=".", label="이상치"
)
plt.plot(line_X, line_y, color="navy", linewidth=lw, label="선형 회귀 분석기")
plt.plot(
    line_X,
    line_y_ransac,
    color="cornflowerblue",
    linewidth=lw,
    label="RANSAC 회귀 분석기",
)
plt.legend(loc="lower right")
plt.xlabel("입력")
plt.ylabel("응답")
plt.show()
```
