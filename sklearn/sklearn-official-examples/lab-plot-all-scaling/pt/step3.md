# Definir Distribuições

Definimos uma lista de diferentes escalonadores, transformadores e normalizadores para colocar os dados dentro de um intervalo pré-definido e armazená-los numa lista chamada distribuições.

```python
# Definir distribuições
distributions = [
    ("Dados não escalonados", X),
    ("Dados após escalonamento padrão", StandardScaler().fit_transform(X)),
    ("Dados após escalonamento min-max", MinMaxScaler().fit_transform(X)),
    ("Dados após escalonamento robusto", RobustScaler(quantile_range=(25, 75)).fit_transform(X)),
    ("Dados após normalização L2 por amostra", Normalizer().fit_transform(X)),
    ("Dados após transformação de quantis (pdf uniforme)", QuantileTransformer(output_distribution="uniform").fit_transform(X)),
    ("Dados após transformação de quantis (pdf gaussiano)", QuantileTransformer(output_distribution="normal").fit_transform(X)),
    ("Dados após transformação de potência (Yeo-Johnson)", PowerTransformer(method="yeo-johnson").fit_transform(X)),
    ("Dados após transformação de potência (Box-Cox)", PowerTransformer(method="box-cox").fit_transform(X)),
]
```
