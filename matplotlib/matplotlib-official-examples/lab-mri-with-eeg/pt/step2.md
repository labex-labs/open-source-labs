# Plotar o Histograma da Intensidade de MRI

Em seguida, plotaremos o histograma da intensidade de MRI usando a função `hist()`. Normalizaremos os valores de intensidade para variar entre 0 e 1.

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
