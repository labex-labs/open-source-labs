# Nachbarn visualisieren

Wir visualisieren nun die Verbindungen zwischen den Datenpunkten, wobei die Dicke der Verbindung zwischen Punkt Nr. 3 und einem anderen Punkt proportional zu ihrer Entfernung ist.

```python
def link_thickness_i(X, i):
    diff_embedded = X[i] - X
    dist_embedded = np.einsum("ij,ij->i", diff_embedded, diff_embedded)
    dist_embedded[i] = np.inf

    # berechne exponentiierte Entfernungen (verwende die log-sum-exp-Methode,
    # um numerische Instabilitäten zu vermeiden)
    exp_dist_embedded = np.exp(-dist_embedded - logsumexp(-dist_embedded))
    return exp_dist_embedded


def relate_point(X, i, ax):
    pt_i = X[i]
    for j, pt_j in enumerate(X):
        thickness = link_thickness_i(X, i)
        if i!= j:
            line = ([pt_i[0], pt_j[0]], [pt_i[1], pt_j[1]])
            ax.plot(*line, c=cm.Set1(y[j]), linewidth=5 * thickness[j])


i = 3
relate_point(X, i, ax)
plt.show()
```
