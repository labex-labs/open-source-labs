# 플롯 생성

다음으로, `imshow`와 `numpy.random`으로 생성된 임의 배열을 사용하여 두 개의 플롯을 생성해 보겠습니다. 또한 플롯에 컬러 바 (color bar) 를 추가할 것입니다. 다음 코드를 실행하세요:

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

plt.subplot(211)
plt.imshow(np.random.random((100, 100)))
plt.subplot(212)
plt.imshow(np.random.random((100, 100)))

cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)

plt.show()
```
