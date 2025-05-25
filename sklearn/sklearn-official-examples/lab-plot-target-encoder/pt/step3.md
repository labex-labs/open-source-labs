# Suporte a Características Categóricas Nativas

Nesta secção, construímos e avaliamos um pipeline que utiliza o suporte nativo a características categóricas em `HistGradientBoostingRegressor`, que suporta apenas até 255 categorias únicas. Agrupamos as características categóricas em características de baixa e alta cardinalidade. As características de alta cardinalidade serão codificadas por alvo, e as características de baixa cardinalidade utilizarão a característica categórica nativa no _gradient boosting_.
