# Tamanho da Figura em Centímetros

Também podemos especificar o tamanho da figura em centímetros. Para fazer isso, precisamos converter os números baseados em centímetros para polegadas. Podemos fazer isso multiplicando o valor em centímetros pelo fator de conversão de cm para polegadas, que é 1/2.54. Em seguida, podemos usar esse valor como o parâmetro `figsize` na função `subplots`. O código abaixo mostra como criar uma figura com um tamanho de 15 cm x 5 cm.

```python
cm = 1/2.54  # centimeters in inches
plt.subplots(figsize=(15*cm, 5*cm))
plt.show()
```
