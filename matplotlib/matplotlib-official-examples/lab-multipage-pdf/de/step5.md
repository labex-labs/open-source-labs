# Erstellen der dritten Seite

In diesem Schritt wirst du die dritte Seite der PDF-Datei erstellen. Die Seite wird einen Plot einer Parabel enthalten.

```python
plt.rcParams['text.usetex'] = False
fig = plt.figure(figsize=(4, 5))
plt.plot(x, x ** 2, 'ko')
plt.title('Page Three')
pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
plt.close()
```
