# Interpretar curvas de calibración

Las curvas de calibración muestran la relación entre las probabilidades predichas y los resultados reales para cada modelo. Los modelos bien calibrados producen curvas que siguen la línea diagonal, lo que indica que las probabilidades predichas coinciden con los resultados reales. Los cuatro modelos producen resultados diferentes:

- La regresión logística produce predicciones bien calibradas ya que optimiza directamente la pérdida logarítmica.
- El Naive Bayes Gaussiano tiende a empujar las probabilidades a 0 o 1, principalmente porque la ecuación de Naive Bayes solo proporciona una estimación correcta de las probabilidades cuando se cumple la suposición de que las características son condicionalmente independientes.
- El Clasificador de Bosque Aleatorio muestra un comportamiento opuesto: los histogramas muestran picos en aproximadamente 0,2 y 0,9 de probabilidad, mientras que las probabilidades cercanas a 0 o 1 son muy raras.
- El SVM Lineal muestra una curva sigmoidea aún más pronunciada que el Clasificador de Bosque Aleatorio, lo que es típico de los métodos de márgenes máximos.
