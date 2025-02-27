# Creación de transformadores

Crearemos transformadores que extraigan características del conjunto de datos. Definiremos dos funciones que realicen la transformación de los datos y luego usaremos `FunctionTransformer` de Scikit-Learn para crear los transformadores.

```python
def subject_body_extractor(posts):
    # construye un arreglo de tipo objeto con dos columnas
    # primera columna = 'asunto' y segunda columna = 'cuerpo'
    features = np.empty(shape=(len(posts), 2), dtype=object)
    for i, text in enumerate(posts):
        # variable temporal `_` almacena '\n\n'
        headers, _, body = text.partition("\n\n")
        # almacena el texto del cuerpo en la segunda columna
        features[i, 1] = body

        prefijo = "Asunto:"
        sub = ""
        # guarda el texto después de 'Asunto:' en la primera columna
        for linea in headers.split("\n"):
            if linea.startswith(prefijo):
                sub = linea[len(prefijo) :]
                break
        features[i, 0] = sub

    return features

subject_body_transformer = FunctionTransformer(subject_body_extractor)

def text_stats(posts):
    return [{"longitud": len(text), "num_oraciones": text.count(".")} for text in posts]

text_stats_transformer = FunctionTransformer(text_stats)
```
