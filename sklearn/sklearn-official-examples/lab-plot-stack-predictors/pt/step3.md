# Empilhamento de preditores em um único conjunto de dados

Agora podemos usar o conjunto de dados Ames Housing para fazer as previsões. Verificamos o desempenho de cada preditor individual, bem como do empilhamento dos regressores. Combinamos 3 aprendizes (lineares e não lineares) e usamos um regressor de ridge para combinar suas saídas. O regressor empilhado combinará as forças dos diferentes regressores. No entanto, também observamos que treinar o regressor empilhado é muito mais caro computacionalmente.
