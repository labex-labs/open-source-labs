# Global Title Positioning with RCParams

In this final step, you'll learn how to use Matplotlib's runtime configuration parameters (RCParams) to set global defaults for title positioning. This is useful when you want all plots in your notebook or script to use consistent title positioning without having to specify it for each plot individually.

## Understanding RCParams in Matplotlib

Matplotlib's behavior can be customized using a dictionary-like variable called `rcParams`. This allows you to set global defaults for various properties, including title positioning.

## Setting Global Title Positioning with rcParams

Let's set global defaults for title positioning and then create some plots that will automatically use these settings:

```python
# View the current default values
print("Default title y position:", plt.rcParams['axes.titley'])
print("Default title padding:", plt.rcParams['axes.titlepad'])
```

Run the cell to see the default values. Now, let's modify these settings:

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

Run the cell. Notice how the title is positioned according to the global settings we defined, even though we didn't specify any positioning parameters in the `title()` function.

## Creating Multiple Plots with the Same Settings

Let's create several plots that all use our global settings:

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

Run the cell. All four subplot titles should be positioned according to the global settings we defined earlier.

## Resetting RCParams to Defaults

If you want to reset the RCParams to their default values, you can use the `rcdefaults()` function:

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

Run the cell. The title should now be positioned using Matplotlib's default settings.

## Temporary RCParams Changes

If you want to temporarily change RCParams for just a specific section of your code, you can use a context manager:

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

Run the cell. You should see three plots:

1. The first with default title positioning
2. The second with right-aligned and higher positioned title (due to the temporary settings)
3. The third with default title positioning again (as the temporary settings only applied within the context manager)

This approach allows you to make temporary changes to the global settings without affecting the rest of your plots.
