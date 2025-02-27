# Theoretische Grenzen (Fortsetzung)

Das zweite Diagramm zeigt, dass eine Erhöhung der zulässigen Verzerrung `eps` es uns ermöglicht, die minimale Anzahl an Dimensionen `n_components` für eine gegebene Anzahl von Proben `n_samples` zu verringern.

```python
# Bereich der zulässigen Verzerrungen
eps_range = np.linspace(0.01, 0.99, 100)

# Bereich der Anzahl von Proben (Beobachtungen) zum Einbetten
n_samples_range = np.logspace(2, 6, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(n_samples_range)))

plt.figure()
for n_samples, color in zip(n_samples_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples, eps=eps_range)
    plt.semilogy(eps_range, min_n_components, color=color)

plt.legend([f"n_samples = {n}" for n in n_samples_range], loc="upper right")
plt.xlabel("Verzerrung eps")
plt.ylabel("Minimale Anzahl an Dimensionen")
plt.title("Johnson-Lindenstrauss-Grenzen:\nn_components vs eps")
plt.show()
```
