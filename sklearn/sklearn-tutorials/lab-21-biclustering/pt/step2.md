# Executar Co-Clustering Espectral

Agora, vamos realizar o biclustering utilizando o algoritmo de Co-Clustering Espectral. Este algoritmo encontra biclusters com valores mais elevados em comparação com outras linhas e colunas.

```python
# Inicializar e ajustar o modelo de Co-Clustering Espectral
model_co = SpectralCoclustering(n_clusters=3, random_state=0)
model_co.fit(data)

# Obter a associação de clusters de linhas e colunas
row_clusters_co = model_co.row_labels_
column_clusters_co = model_co.column_labels_
```
