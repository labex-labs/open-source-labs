# Créer le diagramme SkewT-logP

Nous allons maintenant créer le diagramme SkewT-logP en utilisant la projection SkewXAxes que nous avons enregistrée précédemment. Nous allons tout d'abord créer un objet figure et ajouter un sous-graphique avec la projection SkewXAxes. Nous tracerons ensuite les données de température et de point de rosée sur le diagramme en utilisant la fonction semilogy. Enfin, nous définirons les limites et les graduations pour l'axe X et l'axe Y et afficherons le tracé.

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```
