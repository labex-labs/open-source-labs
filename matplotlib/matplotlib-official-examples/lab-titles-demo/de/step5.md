# Globale Titelpositionierung mit RCParams

In diesem letzten Schritt lernen Sie, wie Sie Matplotlibs Laufzeitkonfigurationsparameter (RCParams) verwenden können, um globale Standardwerte für die Titelpositionierung festzulegen. Dies ist nützlich, wenn Sie möchten, dass alle Diagramme in Ihrem Notebook oder Skript eine konsistente Titelpositionierung verwenden, ohne dass Sie dies für jedes Diagramm individuell angeben müssen.

## Grundlegendes zu RCParams in Matplotlib

Das Verhalten von Matplotlib kann mithilfe einer wörterbuchähnlichen Variable namens `rcParams` angepasst werden. Dies ermöglicht es Ihnen, globale Standardwerte für verschiedene Eigenschaften festzulegen, einschließlich der Titelpositionierung.

## Festlegen der globalen Titelpositionierung mit rcParams

Legen wir globale Standardwerte für die Titelpositionierung fest und erstellen dann einige Diagramme, die automatisch diese Einstellungen verwenden:

```python
# View the current default values
print("Default title y position:", plt.rcParams['axes.titley'])
print("Default title padding:", plt.rcParams['axes.titlepad'])
```

Führen Sie die Zelle aus, um die Standardwerte anzuzeigen. Jetzt ändern wir diese Einstellungen:

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

Führen Sie die Zelle aus. Beachten Sie, wie der Titel gemäß den von uns definierten globalen Einstellungen positioniert wird, obwohl wir keine Positionierungsparameter in der `title()`-Funktion angegeben haben.

## Erstellen mehrerer Diagramme mit denselben Einstellungen

Erstellen wir mehrere Diagramme, die alle unsere globalen Einstellungen verwenden:

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

Führen Sie die Zelle aus. Alle vier Teil-Diagramm-Titel sollten gemäß den von uns zuvor definierten globalen Einstellungen positioniert sein.

## Zurücksetzen der RCParams auf die Standardwerte

Wenn Sie die RCParams auf ihre Standardwerte zurücksetzen möchten, können Sie die Funktion `rcdefaults()` verwenden:

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

Führen Sie die Zelle aus. Der Titel sollte jetzt unter Verwendung der Standard-Einstellungen von Matplotlib positioniert sein.

## Temporäre Änderungen der RCParams

Wenn Sie die RCParams nur für einen bestimmten Abschnitt Ihres Codes temporär ändern möchten, können Sie einen Kontext-Manager verwenden:

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

Führen Sie die Zelle aus. Sie sollten drei Diagramme sehen:

1. Das erste mit der Standard-Titelpositionierung
2. Das zweite mit einem rechtsbündigen und höher positionierten Titel (aufgrund der temporären Einstellungen)
3. Das dritte wieder mit der Standard-Titelpositionierung (da die temporären Einstellungen nur innerhalb des Kontext-Managers gelten)

Dieser Ansatz ermöglicht es Ihnen, temporäre Änderungen an den globalen Einstellungen vorzunehmen, ohne die restlichen Diagramme zu beeinflussen.
