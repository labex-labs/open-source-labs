# Carga y Examen de la Imagen

Ahora que hemos importado nuestras bibliotecas, necesitamos cargar la imagen que queremos superponer en nuestro gráfico. Matplotlib proporciona algunas imágenes de muestra que podemos utilizar para practicar.

1. Crea una nueva celda en tu cuaderno (notebook) e introduce el siguiente código:

```python
# Load the sample image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Display information about the image
print(f"Image shape: {im.shape}")
print(f"Image data type: {im.dtype}")

# Display the image
plt.figure(figsize=(4, 4))
plt.imshow(im)
plt.axis('off')  # Hide axis
plt.title('Matplotlib Logo')
plt.show()
```

Este código hace lo siguiente:

- Utiliza `cbook.get_sample_data()` para cargar una imagen de muestra llamada 'logo2.png' de la colección de datos de muestra de Matplotlib.
- Utiliza `image.imread()` para leer el archivo de imagen en una matriz NumPy.
- Imprime información sobre las dimensiones y el tipo de datos de la imagen.
- Crea una figura y muestra la imagen utilizando `plt.imshow()`.
- Oculta las marcas y etiquetas del eje con `plt.axis('off')`.
- Agrega un título a la figura.
- Muestra la figura utilizando `plt.show()`.

2. Ejecuta la celda presionando Shift+Enter.

La salida debe mostrar información sobre la imagen y mostrar el logotipo de Matplotlib. La forma de la imagen indica las dimensiones de la misma (altura, ancho, canales de color), y el tipo de datos nos dice cómo se almacenan los datos de la imagen.

![image-info](../assets/screenshot-20250306-cqkw4mpg@2x.png)

Este paso es importante porque nos ayuda a entender la imagen que usaremos como superposición. Podemos ver su apariencia y dimensiones, lo cual será útil a la hora de decidir cómo posicionarla en nuestro gráfico.
