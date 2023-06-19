# Define Allowed Values for the Amplitude Slider

In this step, you will define the allowed values for the amplitude slider. The amplitude slider will use these values to snap to the nearest allowed value.

```python
# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])
```
