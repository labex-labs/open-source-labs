# 대상 분포 플롯

로그 함수를 적용하기 전후의 대상 확률 밀도 함수를 플롯합니다.

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_xlim([0, 2000])
ax0.set_ylabel("확률")
ax0.set_xlabel("대상")
ax0.set_title("대상 분포")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("확률")
ax1.set_xlabel("대상")
ax1.set_title("변환된 대상 분포")

f.suptitle("합성 데이터", y=1.05)
plt.tight_layout()
```
