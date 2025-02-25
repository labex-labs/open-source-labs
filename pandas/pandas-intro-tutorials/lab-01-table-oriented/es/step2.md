# Crear un DataFrame

Los datos en pandas se almacenan en un DataFrame, que es una estructura de datos etiquetada bidimensional con columnas que pueden ser de diferentes tipos.

```python
# Creando un DataFrame
df = pd.DataFrame(
    {
        "Nombre": [
            "Braund, Sr. Owen Harris",
            "Allen, Sr. William Henry",
            "Bonnell, Sra. Elizabeth",
        ],
        "Edad": [22, 35, 58],
        "Sexo": ["masculino", "masculino", "femenino"],
    }
)
```
