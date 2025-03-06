# Глобальное позиционирование заголовков с использованием RCParams

На этом последнем этапе вы узнаете, как использовать параметры времени выполнения (RCParams) Matplotlib для установки глобальных значений по умолчанию для позиционирования заголовков. Это полезно, когда вы хотите, чтобы все графики в вашем блокноте или скрипте использовали единообразное позиционирование заголовков, не требуя его указания для каждого графика отдельно.

## Понимание RCParams в Matplotlib

Поведение Matplotlib можно настроить с помощью переменной, похожей на словарь, называемой `rcParams`. Это позволяет вам устанавливать глобальные значения по умолчанию для различных свойств, включая позиционирование заголовков.

## Установка глобального позиционирования заголовков с помощью rcParams

Установим глобальные значения по умолчанию для позиционирования заголовков, а затем создадим несколько графиков, которые автоматически будут использовать эти настройки:

```python
# View the current default values
print("Default title y position:", plt.rcParams['axes.titley'])
print("Default title padding:", plt.rcParams['axes.titlepad'])
```

Запустите ячейку, чтобы увидеть значения по умолчанию. Теперь изменим эти настройки:

```python
# Set new global defaults for title positioning
plt.rcParams['axes.titley'] = 1.05     # Set title y position higher
plt.rcParams['axes.titlepad'] = 10     # Set padding between title and plot
plt.rcParams['axes.titlelocation'] = 'left'  # Set default alignment to left

# Create a plot that will use the new defaults
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Global RCParams Settings')
plt.show()
```

Запустите ячейку. Обратите внимание, как заголовок позиционируется в соответствии с глобальными настройками, которые мы определили, даже несмотря на то, что мы не указали никаких параметров позиционирования в функции `title()`.

## Создание нескольких графиков с одинаковыми настройками

Создадим несколько графиков, все из которых будут использовать наши глобальные настройки:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot with titles that use global settings
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1} Using Global Settings')

plt.tight_layout()
plt.show()
```

Запустите ячейку. Все четыре заголовка подграфиков должны быть позиционированы в соответствии с глобальными настройками, которые мы определили ранее.

## Сброс RCParams до значений по умолчанию

Если вы хотите сбросить RCParams до значений по умолчанию, вы можете использовать функцию `rcdefaults()`:

```python
# Reset to default settings
plt.rcdefaults()

# Create a plot with default settings
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Default Settings Again')
plt.show()
```

Запустите ячейку. Теперь заголовок должен быть позиционирован с использованием значений по умолчанию Matplotlib.

## Временные изменения RCParams

Если вы хотите временно изменить RCParams только для определенной части вашего кода, вы можете использовать менеджер контекста:

```python
# Create a plot with default settings
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Default Settings')
plt.show()

# Temporarily change RCParams for just this section
with plt.rc_context({'axes.titlelocation': 'right', 'axes.titley': 1.1}):
    plt.figure(figsize=(8, 5))
    plt.plot(range(10))
    plt.grid(True)
    plt.title('Temporary Settings Change')
    plt.show()

# Create another plot that will use default settings again
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Back to Default Settings')
plt.show()
```

Запустите ячейку. Вы должны увидеть три графика:

1. Первый с позиционированием заголовка по умолчанию.
2. Второй с заголовком, выровненным по правому краю и расположенным выше (из - за временных настроек).
3. Третий снова с позиционированием заголовка по умолчанию (так как временные настройки применялись только внутри менеджера контекста).

Этот подход позволяет вам вносить временные изменения в глобальные настройки без влияния на остальные графики.
