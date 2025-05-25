# Personalizar o Gráfico

Podemos personalizar o gráfico ainda mais adicionando rótulos aos eixos e um título. Também podemos alterar a cor dos rótulos dos eixos e do título da legenda. O código a seguir demonstra como personalizar o gráfico:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```
