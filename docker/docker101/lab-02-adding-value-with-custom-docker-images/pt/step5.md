# Implantando uma Mudança

O aplicativo "hello world!" é superestimado, vamos atualizar o aplicativo para que ele diga "Hello Beautiful World!" em vez disso.

## Atualizar `app.py`

Substitua a string "Hello World" por "Hello Beautiful World!" em `app.py`. Você pode atualizar o arquivo com o seguinte comando. (copie e cole todo o bloco de código)

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello beautiful world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

## Reconstruir e Enviar sua Imagem

Agora que seu aplicativo está atualizado, você precisa repetir as etapas acima para reconstruir seu aplicativo e enviá-lo para o registro do Docker Hub.

Primeiro, reconstrua, desta vez use seu nome de usuário do Docker Hub no comando de build:

```bash
docker image build -t $DOCKERHUB_USERNAME/python-hello-world .
```

Observe "Using cache" (Usando cache) para as etapas 1-3. Essas camadas da Imagem Docker já foram construídas e `docker image build` usará essas camadas do cache em vez de reconstruí-las.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

Existe um mecanismo de cache em vigor também para enviar camadas. O Docker Hub já possui todas as camadas, exceto uma, de um envio anterior, então ele envia apenas a camada que foi alterada.

Quando você altera uma camada, cada camada construída em cima dela terá que ser reconstruída. Cada linha em um Dockerfile constrói uma nova camada que é construída na camada criada a partir das linhas anteriores. É por isso que a ordem das linhas em nosso Dockerfile é importante. Otimizamos nosso Dockerfile para que a camada com maior probabilidade de mudar (`COPY app.py /app.py`) seja a última linha do Dockerfile. Geralmente, para um aplicativo, seu código muda com a taxa mais frequente. Essa otimização é particularmente importante para processos CI/CD, onde você deseja que sua automação seja executada o mais rápido possível.
