# Crear la figura 1

Comenzaremos creando la primera figura, que contendrá dos subgráficos. Graficaremos la primera onda senoidal en el subgráfico superior y el doble de la amplitud de la primera onda senoidal en el subgráfico inferior.

```python
plt.figure(1)

# Subgráfico superior
plt.subplot(211)
plt.plot(t, s1)

# Subgráfico inferior
plt.subplot(212)
plt.plot(t, 2*s1)
```
