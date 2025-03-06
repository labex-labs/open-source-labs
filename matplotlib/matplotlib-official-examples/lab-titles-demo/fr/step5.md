# Positionnement global des titres avec RCParams

Dans cette étape finale, vous apprendrez à utiliser les paramètres de configuration runtime (RCParams) de Matplotlib pour définir des valeurs par défaut globales pour le positionnement des titres. Cela est utile lorsque vous souhaitez que tous les graphiques de votre notebook ou de votre script utilisent un positionnement de titre cohérent sans avoir à le spécifier pour chaque graphique individuellement.

## Comprendre les RCParams dans Matplotlib

Le comportement de Matplotlib peut être personnalisé à l'aide d'une variable semblable à un dictionnaire appelée `rcParams`. Cela vous permet de définir des valeurs par défaut globales pour diverses propriétés, y compris le positionnement des titres.

## Définition du positionnement global des titres avec rcParams

Définissons des valeurs par défaut globales pour le positionnement des titres, puis créons quelques graphiques qui utiliseront automatiquement ces paramètres :

```python
# View the current default values
print("Default title y position:", plt.rcParams['axes.titley'])
print("Default title padding:", plt.rcParams['axes.titlepad'])
```

Exécutez la cellule pour voir les valeurs par défaut. Maintenant, modifions ces paramètres :

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

Exécutez la cellule. Remarquez comment le titre est positionné selon les paramètres globaux que nous avons définis, même si nous n'avons spécifié aucun paramètre de positionnement dans la fonction `title()`.

## Création de plusieurs graphiques avec les mêmes paramètres

Créons plusieurs graphiques qui utilisent tous nos paramètres globaux :

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

Exécutez la cellule. Tous les quatre titres de sous - graphiques devraient être positionnés selon les paramètres globaux que nous avons définis précédemment.

## Réinitialisation des RCParams aux valeurs par défaut

Si vous souhaitez réinitialiser les RCParams à leurs valeurs par défaut, vous pouvez utiliser la fonction `rcdefaults()` :

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

Exécutez la cellule. Le titre devrait maintenant être positionné en utilisant les paramètres par défaut de Matplotlib.

## Changements temporaires des RCParams

Si vous souhaitez modifier temporairement les RCParams pour une section spécifique de votre code, vous pouvez utiliser un gestionnaire de contexte :

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

Exécutez la cellule. Vous devriez voir trois graphiques :

1. Le premier avec le positionnement de titre par défaut
2. Le deuxième avec un titre aligné à droite et positionné plus haut (en raison des paramètres temporaires)
3. Le troisième avec le positionnement de titre par défaut à nouveau (car les paramètres temporaires n'ont été appliqués qu'au sein du gestionnaire de contexte)

Cette approche vous permet de modifier temporairement les paramètres globaux sans affecter le reste de vos graphiques.
