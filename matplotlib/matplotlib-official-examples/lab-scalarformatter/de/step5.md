# Konfigurieren der Skalenbeschriftungsformatierung

Wir werden die Skalenbeschriftungsformatierung für unsere Teilplots konfigurieren. Der erste Teilplot wird die Standardeinstellungen verwenden, der zweite Teilplot wird eine ansprechende Formatierung von mathematischen Ausdrücken verwenden und der dritte Teilplot wird keine Offsetnotation verwenden.

```python
# Subplot 1 (Standardeinstellungen)
axs[0, 0].set_title("Standardeinstellungen")

# Subplot 2 (useMathText=True)
for ax in axs[:, 1]:
    ax.ticklabel_format(useMathText=True)
axs[0, 1].set_title("useMathText=True")

# Subplot 3 (useOffset=False)
for ax in axs[:, 2]:
    ax.ticklabel_format(useOffset=False)
axs[0, 2].set_title("useOffset=False")
```
