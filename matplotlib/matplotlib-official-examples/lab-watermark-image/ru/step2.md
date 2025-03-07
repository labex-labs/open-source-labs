# Загрузка и изучение изображения

Теперь, когда мы импортировали наши библиотеки, нам нужно загрузить изображение, которое мы хотим наложить на наш график. Matplotlib предоставляет несколько примеров изображений, которые мы можем использовать для практики.

1. Создайте новую ячейку в своем ноутбуке и введите следующий код:

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

Этот код выполняет следующие действия:

- Использует `cbook.get_sample_data()`, чтобы загрузить образец изображения с именем 'logo2.png' из коллекции примеров данных Matplotlib.
- Использует `image.imread()`, чтобы прочитать файл изображения в массив NumPy.
- Выводит информацию о размерах изображения и типе данных.
- Создает фигуру и отображает изображение с помощью `plt.imshow()`.
- Скрывает деления и метки осей с помощью `plt.axis('off')`.
- Добавляет заголовок к фигуре.
- Отображает фигуру с помощью `plt.show()`.

2. Запустите ячейку, нажав Shift+Enter.

В выводе должны отобразиться информация о изображении и показан логотип Matplotlib. Форма изображения указывает размеры изображения (высота, ширина, цветовые каналы), а тип данных говорит о том, как хранятся данные изображения.

![image-info](../assets/screenshot-20250306-cqkw4mpg@2x.png)

Этот шаг важен, так как он помогает нам понять, какое изображение мы будем использовать в качестве наложения. Мы можем увидеть его внешний вид и размеры, что будет полезно при решении вопроса о том, как разместить его на нашем графике.
