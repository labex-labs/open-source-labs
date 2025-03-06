# Erstellen einer abschließenden Visualisierung mit mehreren Textelementen

In diesem letzten Schritt werden wir alles, was wir gelernt haben, kombinieren, um eine umfassende Visualisierung zu erstellen, die mehrere Textelemente mit unterschiedlichen Stilen enthält. Dies wird zeigen, wie Textboxen zur Verbesserung der Datenstorytelling eingesetzt werden können.

## Erstellen einer fortgeschrittenen Visualisierung

Wir erstellen ein anspruchsvolleres Diagramm, das sowohl unser Histogramm als auch einige zusätzliche visuelle Elemente enthält. Geben Sie in einer neuen Zelle den folgenden Code ein und führen Sie ihn aus:

```python
# Create a figure with a larger size for our final visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with more bins and a different color
n, bins, patches = ax.hist(x, bins=75, color='lightblue',
                           edgecolor='darkblue', alpha=0.7)

# Add title and labels with improved styling
ax.set_title('Distribution of Random Data with Statistical Annotations',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Mark the mean with a vertical line
ax.axvline(x=mu, color='red', linestyle='-', linewidth=2,
           label=f'Mean: {mu:.2f}')

# Mark one standard deviation range
ax.axvline(x=mu + sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean + 1σ: {mu+sigma:.2f}')
ax.axvline(x=mu - sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean - 1σ: {mu-sigma:.2f}')

# Create a text box with statistics in the top left
stats_box_props = dict(boxstyle='round', facecolor='lightyellow',
                      alpha=0.8, edgecolor='gold', linewidth=2)

stats_text = '\n'.join((
    r'$\mathbf{Statistics:}$',
    r'$\mu=%.2f$ (mean)' % (mu,),
    r'$\mathrm{median}=%.2f$' % (median,),
    r'$\sigma=%.2f$ (std. dev.)' % (sigma,)
))

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=stats_box_props)

# Add an informational text box in the top right
info_box_props = dict(boxstyle='round4', facecolor='lightcyan',
                     alpha=0.8, edgecolor='deepskyblue', linewidth=2)

info_text = '\n'.join((
    r'$\mathbf{About\ Normal\ Distributions:}$',
    r'$\bullet\ 68\%\ of\ data\ within\ 1\sigma$',
    r'$\bullet\ 95\%\ of\ data\ within\ 2\sigma$',
    r'$\bullet\ 99.7\%\ of\ data\ within\ 3\sigma$'
))

ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=info_box_props)

# Add a legend
ax.legend(fontsize=12)

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()
```

Wenn Sie diese Zelle ausführen, sehen Sie eine umfassende Visualisierung mit:

- Einem Histogramm der Daten mit verbessertem Stil
- Vertikalen Linien, die den Mittelwert und den Bereich einer Standardabweichung markieren
- Einer Statistik-Textbox in der oberen linken Ecke
- Einer Informations-Textbox über Normalverteilungen in der oberen rechten Ecke
- Einer Legende, die die vertikalen Linien erklärt

## Verständnis der fortgeschrittenen Elemente

Lassen Sie uns einige der neuen Elemente untersuchen, die wir hinzugefügt haben:

1. **Vertikale Linien mit `axvline()`**:

   - Diese Linien markieren wichtige Statistiken direkt im Diagramm.
   - Der `label`-Parameter ermöglicht es, diese Linien in die Legende aufzunehmen.

2. **Mehrere Textboxen mit unterschiedlichen Stilen**:

   - Jede Textbox hat einen anderen Zweck und verwendet einen eigenen Stil.
   - Die Statistik-Box zeigt die berechneten Werte aus unseren Daten.
   - Die Informations-Box gibt Kontext zu Normalverteilungen.

3. **Verbesserte Formatierung**:

   - LaTeX-Formatierung wird verwendet, um fett gedruckten Text mit `\mathbf{}` zu erstellen.
   - Aufzählungszeichen werden mit `\bullet` erstellt.
   - Der Abstand wird mit `\ ` (Backslash gefolgt von einem Leerzeichen) gesteuert.

4. **Gitter und Legende**:
   - Das Gitter hilft den Betrachtern, Werte aus dem Diagramm genauer abzulesen.
   - Die Legende erklärt die Bedeutung der farbigen Linien.

## Abschließende Anmerkungen zur Textbox-Platzierung

Beim Platzieren mehrerer Textelemente in einer Visualisierung sollten Sie Folgendes berücksichtigen:

1. **Visuelle Hierarchie**: Die wichtigste Information sollte am stärksten hervorstechen.
2. **Platzierung**: Platzieren Sie verwandte Informationen in der Nähe der relevanten Teile der Visualisierung.
3. **Kontrast**: Stellen Sie sicher, dass der Text gegen seinen Hintergrund lesbar ist.
4. **Konsistenz**: Verwenden Sie einen konsistenten Stil für ähnliche Arten von Informationen.
5. **Überfüllung**: Vermeiden Sie es, die Visualisierung mit zu vielen Textelementen zu überfüllen.

Durch die gedankenvollen Platzierung und Gestaltung von Textboxen können Sie Visualisierungen erstellen, die sowohl informativ als auch visuell ansprechend sind und die Betrachter dabei helfen, die wichtigsten Erkenntnisse aus Ihren Daten zu verstehen.
