# Soporte nativo para características categóricas

En esta sección, construimos y evaluamos una tubería que utiliza el soporte nativo para características categóricas en `HistGradientBoostingRegressor`, que solo admite hasta 255 categorías únicas. Agrupamos las características categóricas en características de baja cardinalidad y características de alta cardinalidad. Las características de alta cardinalidad se codificarán con el target y las características de baja cardinalidad utilizarán la característica categórica nativa en el boosting de gradiente.
