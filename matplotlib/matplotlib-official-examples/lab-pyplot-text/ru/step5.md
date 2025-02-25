# Добавление заголовка, меток по оси X и оси Y

Мы можем добавить заголовок, метку по оси X и метку по оси Y к графику с использованием методов `title()`, `xlabel()` и `ylabel()` библиотеки `pyplot`. Мы добавим "Voltage vs Time" в качестве заголовка, "Time [s]" в качестве метки по оси X и "Voltage [mV]" в качестве метки по оси Y.

```python
plt.title(r'Voltage vs Time', fontsize=20)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
```
