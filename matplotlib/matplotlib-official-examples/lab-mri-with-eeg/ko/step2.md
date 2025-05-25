# MRI 강도 히스토그램 플롯

다음으로, `hist()` 함수를 사용하여 MRI 강도의 히스토그램을 플롯합니다. 강도 값을 0 과 1 사이로 정규화합니다.

```python
# Plot the histogram of MRI intensity
ax1 = fig.add_subplot(2, 2, 2)
im = np.ravel(im)
im = im[np.nonzero(im)]  # Ignore the background
im = im / im.max()  # Normalize
ax1.hist(im, bins=100)
ax1.set_xlabel('Intensity (a.u.)')
ax1.set_ylabel('MRI density')
```
