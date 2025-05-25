# Executar Biclustering Espectral

Em seguida, vamos realizar o biclustering utilizando o algoritmo de Biclustering Espectral. Este algoritmo pressupõe que a matriz de dados possui uma estrutura de tabuleiro de xadrez oculta.

```python
# Inicializar e ajustar o modelo de Biclustering Espectral
model_bi = SpectralBiclustering(n_clusters=(2, 3), random_state=0)
model_bi.fit(data)

# Obter a associação de clusters de linhas e colunas
row_clusters_bi = model_bi.row_labels_
column_clusters_bi = model_bi.column_labels_
```
