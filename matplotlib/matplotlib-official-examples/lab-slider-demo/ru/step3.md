# Создание начального графика

Теперь мы создадим начальный график синусоидальной волны. Мы определим начальные параметры для амплитуды и частоты и построим синусоидальную волну с использованием этих параметров.

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```
