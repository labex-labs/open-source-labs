# Gerar Novas Amostras

Usamos o melhor estimador para amostrar 44 novos pontos dos dados. Em seguida, transformamos os novos dados de volta para suas 64 dimensões originais usando a inversa da PCA.

```python
# amostrar 44 novos pontos dos dados
new_data = kde.sample(44, random_state=0)
new_data = pca.inverse_transform(new_data)
```
