# 결과 플롯

Matplotlib 을 사용하여 정규화 강도에 따른 계수 및 오차를 플롯합니다.

```python
plt.figure(figsize=(20, 6))

plt.subplot(121)
ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale("log")
plt.xlabel("alpha")
plt.ylabel("weights")
plt.title("정규화에 따른 Ridge 계수")
plt.axis("tight")

plt.subplot(122)
ax = plt.gca()
ax.plot(alphas, errors)
ax.set_xscale("log")
plt.xlabel("alpha")
plt.ylabel("오차")
plt.title("정규화에 따른 계수 오차")
plt.axis("tight")

plt.show()
```
