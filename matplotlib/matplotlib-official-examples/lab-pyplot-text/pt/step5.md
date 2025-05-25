# Adicionando Título, Rótulo X e Rótulo Y

Podemos adicionar título, rótulo X e rótulo Y ao gráfico usando os métodos `title()`, `xlabel()` e `ylabel()` da biblioteca `pyplot`. Adicionaremos "Voltage vs Time" como título, "Time [s]" como rótulo X e "Voltage [mV]" como rótulo Y.

```python
plt.title(r'Voltage vs Time', fontsize=20)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
```
