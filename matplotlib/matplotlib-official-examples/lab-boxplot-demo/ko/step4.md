# 상자 그림 사용자 정의

상자, 수염 (whiskers), 이상치 (outliers) 의 모양을 변경하여 상자 그림을 사용자 정의할 수 있습니다. 또한, 동일한 플롯에 여러 상자 그림을 생성하여 서로 다른 데이터 그룹을 비교할 수 있습니다. 다음은 상자 그림을 사용자 정의하는 몇 가지 예입니다.

```python
# 노치 (notched) 상자 그림 생성
plt.boxplot(data, notch=True)
plt.show()

# 이상치 점 기호를 녹색 다이아몬드로 변경
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# 수평 상자 그림 생성
plt.boxplot(data, vert=False)
plt.show()

# 하나의 플롯에 여러 상자 그림 생성
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```
