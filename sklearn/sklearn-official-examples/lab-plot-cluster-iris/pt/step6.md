# Avaliar o Clustering

Para avaliar o desempenho do algoritmo K-Means Clustering, podemos calcular a pontuação de inércia. A pontuação de inércia mede a soma das distâncias entre cada ponto de dados e o centro do cluster atribuído. Uma pontuação de inércia mais baixa indica um melhor agrupamento.

```python
print("Pontuação de Inércia:", kmeans.inertia_)
```
