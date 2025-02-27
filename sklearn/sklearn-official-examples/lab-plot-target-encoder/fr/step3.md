# Prise en charge native des fonctionnalités catégorielles

Dans cette section, nous construisons et évaluons un pipeline qui utilise la prise en charge native des fonctionnalités catégorielles dans `HistGradientBoostingRegressor`, qui ne prend en charge que jusqu'à 255 catégories uniques. Nous regroupons les fonctionnalités catégorielles en fonctionnalités à cardinalité faible et à cardinalité élevée. Les fonctionnalités à cardinalité élevée seront encodées cible et les fonctionnalités à cardinalité faible utiliseront la fonctionnalité catégorielle native dans le gradient boosting.
