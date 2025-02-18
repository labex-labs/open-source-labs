# Afficher l'image

Affichez l'image finale en utilisant le code suivant :

```python
ax1.imshow([[0, 1, 2], [1, 2, 3]], cmap=plt.cm.gist_gray_r,
               interpolation="bilinear", aspect="auto")
plt.show()
```
