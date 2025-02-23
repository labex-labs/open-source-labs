# Desplegando un cambio

La aplicación "hello world!" está sobrevalorada, actualicemos la aplicación para que diga "Hello Beautiful World!" en lugar de eso.

## Actualiza `app.py`

Reemplaza la cadena "Hello World" con "Hello Beautiful World!" en `app.py`. Puedes actualizar el archivo con el siguiente comando. (Copiar y pegar todo el bloque de código)

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello beautiful world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

## Vuelve a construir y sube tu imagen

Ahora que tu aplicación está actualizada, debes repetir los pasos anteriores para volver a construir tu aplicación y subirla al registro de Docker Hub.

Primero, vuelve a construir, esta vez usa tu nombre de usuario de Docker Hub en el comando de construcción:

```bash
docker image build -t $DOCKERHUB_USERNAME/python-hello-world.
```

Observa "Using cache" para los pasos 1-3. Estas capas de la imagen de Docker ya se han construido y `docker image build` usará estas capas de la memoria caché en lugar de reconstruirlas.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

También hay un mecanismo de caché para subir capas. Docker Hub ya tiene todas las capas excepto una de una subida anterior, por lo que solo sube la capa que ha cambiado.

Cuando cambias una capa, todas las capas construidas encima de esa tendrán que ser reconstruidas. Cada línea en un Dockerfile construye una nueva capa que se construye sobre la capa creada a partir de las líneas anteriores. Por eso es importante el orden de las líneas en nuestro Dockerfile. Optimizamos nuestro Dockerfile para que la capa que es más probable que cambie (`COPY app.py /app.py`) sea la última línea del Dockerfile. En general, para una aplicación, tus cambios de código son los que más frecuentemente cambian. Esta optimización es particularmente importante para los procesos de CI/CD, donde quieres que tu automatización funcione lo más rápido posible.
