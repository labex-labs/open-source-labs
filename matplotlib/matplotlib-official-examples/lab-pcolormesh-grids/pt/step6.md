# Sombreamento Automático (Auto Shading)

É possível que o usuário queira que o código escolha automaticamente qual sombreamento usar; neste caso, `shading='auto'` decidirá se deve usar o sombreamento `flat` ou `nearest` com base nos formatos de `X`, `Y` e `Z`. Podemos visualizar a grade usando o seguinte bloco de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, shading='auto', cmap='viridis')
ax.set_title('Auto Shading')
plt.show()
```
