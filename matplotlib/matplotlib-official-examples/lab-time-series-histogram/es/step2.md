# Generar datos

En este paso, generaremos múltiples series de "señales" sinusoidales que se encuentran enterradas debajo de un mayor número de series de "ruido/fondo" de caminata aleatoria. Generaremos caminatas aleatorias gaussianas no sesgadas y señales sinusoidales.

```python
# Fije el estado aleatorio para la reproducibilidad
np.random.seed(19680801)

# Cree algunos datos; una caminata aleatoria 1D + una pequeña fracción de ondas sinusoidales
num_series = 1000
num_points = 100
SNR = 0.10  # Relación señal-ruido
x = np.linspace(0, 4 * np.pi, num_points)

# Genere caminatas aleatorias gaussianas no sesgadas
Y = np.cumsum(np.random.randn(num_series, num_points), axis=-1)

# Genere señales sinusoidales
num_signal = round(SNR * num_series)
phi = (np.pi / 8) * np.random.randn(num_signal, 1)  # pequeño desplazamiento aleatorio
Y[-num_signal:] = (
    np.sqrt(np.arange(num_points))  # factor de escala RMS de la caminata aleatoria
    * (np.sin(x - phi)
       + 0.05 * np.random.randn(num_signal, num_points))  # pequeño ruido aleatorio
)
```
