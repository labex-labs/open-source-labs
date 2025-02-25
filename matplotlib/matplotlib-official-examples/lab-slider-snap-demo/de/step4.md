# Definiere erlaubte Werte für den Amplitude-Schieberegler

In diesem Schritt wirst du die erlaubten Werte für den Amplitude-Schieberegler definieren. Der Amplitude-Schieberegler wird diese Werte verwenden, um auf den nächstgelegenen erlaubten Wert zu springen.

```python
# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])
```
