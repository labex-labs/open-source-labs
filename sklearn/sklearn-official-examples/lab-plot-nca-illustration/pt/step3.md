# Aprender um Embedding

Agora usaremos NCA para aprender um embedding e plotar os pontos após a transformação. Em seguida, usaremos o embedding para encontrar os vizinhos mais próximos.

```python
nca = NeighborhoodComponentsAnalysis(max_iter=30, random_state=0)
nca = nca.fit(X, y)

plt.figure(2)
ax2 = plt.gca()
X_embedded = nca.transform(X)
relate_point(X_embedded, i, ax2)

for i in range(len(X)):
    ax2.text(X_embedded[i, 0], X_embedded[i, 1], str(i), va="center", ha="center")
    ax2.scatter(X_embedded[i, 0], X_embedded[i, 1], s=300, c=cm.Set1(y[[i]]), alpha=0.4)

ax2.set_title("Embedding NCA")
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_yaxis().set_visible(False)
ax2.axis("equal")
plt.show()
```
