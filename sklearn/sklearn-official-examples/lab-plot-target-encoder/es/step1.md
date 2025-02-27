# Carga de datos desde OpenML

Primero, cargamos el conjunto de datos de reseñas de vinos usando la función `fetch_openml` del módulo `scikit-learn.datasets`. Solo usaremos un subconjunto de las características numéricas y categóricas en los datos. Usaremos el siguiente subconjunto de características numéricas y categóricas en los datos: `características_numéricas = ["price"]` y `características_categóricas = ["country", "province", "region_1", "region_2", "variety", "winery"]`.
