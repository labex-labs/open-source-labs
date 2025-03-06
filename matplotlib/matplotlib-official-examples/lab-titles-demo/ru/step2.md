# Позиционирование заголовка слева и справа

Matplotlib позволяет вам размещать заголовок слева или справа от графика с использованием параметра `loc`. На этом этапе вы научитесь выравнивать заголовки по левому и правому краям графиков.

## Создание графика с заголовком, выровненным по левому краю

Создадим график с заголовком, расположенным слева. В новой ячейке введите следующий код:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Left-Aligned Title', loc='left')  # Position the title at the left
plt.show()
```

![left-aligned-title](../assets/screenshot-20250306-9pLPZz36@2x.png)

Запустите ячейку. Обратите внимание, как заголовок теперь выровнен по левому краю графика, а не по центру.

Параметр `loc` в функции `title()` определяет горизонтальное положение заголовка. Установив `loc='left'`, вы сообщаете Matplotlib разместить заголовок слева от графика.

## Создание графика с заголовком, выровненным по правому краю

Теперь создадим другой график с заголовком, расположенным справа. В новой ячейке введите следующий код:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Right-Aligned Title', loc='right')  # Position the title at the right
plt.show()
```

![right-aligned-title](../assets/screenshot-20250306-PpNxbjp2@2x.png)

Запустите ячейку. Теперь заголовок должен быть выровнен по правому краю графика.

## Сравнение различных позиций заголовка

Создадим последовательность из трех графиков, чтобы сравнить разные позиции заголовка (центр, лево и право). В новой ячейке введите следующий код:

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Center-aligned title (default)
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Center Title')

# Plot 2: Left-aligned title
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Left Title', loc='left')

# Plot 3: Right-aligned title
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Right Title', loc='right')

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

![three-title-positions](../assets/screenshot-20250306-EzNR2plC@2x.png)

Запустите ячейку, чтобы увидеть все три позиции заголовка рядом друг с другом. Это визуальное сравнение поможет вам понять, как параметр `loc` влияет на позиционирование заголовка.

Обратите внимание, что при работе с подграфиками мы используем метод `set_title()` для отдельных объектов осей, а не глобальную функцию `plt.title()`.
