# Calcular o Agrupamento

Com os dados e a matriz de conectividade definidos, agora podemos realizar o agrupamento hierárquico. Usaremos a classe `AgglomerativeClustering` do scikit-learn para realizar o agrupamento. Definiremos o número de clusters como 27, que corresponde ao número de moedas na imagem. Usaremos o método de ligação "ward", que minimiza a variância das distâncias entre os clusters que estão a ser fundidos. Também passaremos a matriz de conectividade que criámos na etapa 2.

```python
from sklearn.cluster import AgglomerativeClustering
import time as time

print("Calcular agrupamento hierárquico estruturado...")
st = time.time()
n_clusters = 27  # número de regiões
ward = AgglomerativeClustering(
    n_clusters=n_clusters, linkage="ward", connectivity=connectivity
)
ward.fit(X)
label = np.reshape(ward.labels_, rescaled_coins.shape)
print(f"Tempo decorrido: {time.time() - st:.3f}s")
print(f"Número de pixels: {label.size}")
print(f"Número de clusters: {np.unique(label).size}")
```
