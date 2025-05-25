# Ames 주택 데이터의 타겟 분포 플롯

QuantileTransformer 를 적용하기 전후의 타겟의 확률 밀도 함수를 플롯합니다.

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_ylabel("확률")
ax0.set_xlabel("타겟")
ax0.set_title("타겟 분포")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("확률")
ax1.set_xlabel("타겟")
ax1.set_title("변환된 타겟 분포")

f.suptitle("Ames 주택 데이터: 판매 가격", y=1.05)
plt.tight_layout()
```
