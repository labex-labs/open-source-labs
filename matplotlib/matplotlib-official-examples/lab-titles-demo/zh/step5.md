# 使用 RCParams 进行全局标题定位

在这最后一步中，你将学习如何使用 Matplotlib 的运行时配置参数（RCParams）来设置标题定位的全局默认值。当你希望笔记本或脚本中的所有图表都使用一致的标题定位，而无需为每个图表单独指定时，这非常有用。

## 理解 Matplotlib 中的 RCParams

可以使用一个类似字典的变量 `rcParams` 来定制 Matplotlib 的行为。这使你能够为各种属性设置全局默认值，包括标题定位。

## 使用 rcParams 设置全局标题定位

让我们为标题定位设置全局默认值，然后创建一些会自动使用这些设置的图表：

```python
# View the current default values
print("Default title y position:", plt.rcParams['axes.titley'])
print("Default title padding:", plt.rcParams['axes.titlepad'])
```

运行该单元格以查看默认值。现在，让我们修改这些设置：

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

运行该单元格。注意，即使我们在 `title()` 函数中没有指定任何定位参数，标题也是根据我们定义的全局设置进行定位的。

## 创建使用相同设置的多个图表

让我们创建几个都使用我们全局设置的图表：

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

运行该单元格。所有四个子图的标题都应该根据我们之前定义的全局设置进行定位。

## 将 RCParams 重置为默认值

如果你想将 RCParams 重置为默认值，可以使用 `rcdefaults()` 函数：

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

运行该单元格。现在标题应该使用 Matplotlib 的默认设置进行定位。

## 临时更改 RCParams

如果你只想在代码的特定部分临时更改 RCParams，可以使用上下文管理器：

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

运行该单元格。你应该会看到三个图表：

1. 第一个图表使用默认的标题定位。
2. 第二个图表的标题右对齐且位置更高（由于临时设置）。
3. 第三个图表再次使用默认的标题定位（因为临时设置仅在上下文管理器内生效）。

这种方法允许你临时更改全局设置，而不会影响其他图表。
