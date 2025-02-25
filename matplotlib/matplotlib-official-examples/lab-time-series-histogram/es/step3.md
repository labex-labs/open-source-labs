# Visualizar datos con un gráfico de líneas

En este paso, visualizaremos los datos generados con un gráfico de líneas.

```python
# Grafique las series usando `plot` y un valor pequeño de `alpha`.
# Con esta vista, es muy difícil observar el comportamiento sinusoidal debido a la gran cantidad de series superpuestas.
# También tarda un poco en ejecutarse porque se deben generar muchos artistas individuales.
tic = time.time()
plt.plot(x, Y.T, color="C0", alpha=0.1)
toc = time.time()
plt.title("Gráfico de líneas con alpha")
plt.show()
print(f"{toc-tic:.3f} sec. transcurridos")
```
