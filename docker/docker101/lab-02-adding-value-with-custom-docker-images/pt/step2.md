# Criar e Construir a Imagem Docker

Agora, e se você não tiver o python instalado localmente? Não se preocupe! Porque você não precisa. Uma das vantagens de usar containers é que você pode construir python dentro de seus containers, sem ter python instalado em sua máquina host.

Crie um `Dockerfile` executando o seguinte comando. (copie e cole todo o bloco de código)

```bash
echo 'FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py' > Dockerfile
```

Um Dockerfile lista as instruções necessárias para construir uma imagem docker. Vamos analisar o arquivo acima linha por linha.

**FROM python:3.8-alpine**
Este é o ponto de partida para seu Dockerfile. Todo Dockerfile deve começar com uma linha `FROM` que é a imagem inicial para construir suas camadas em cima.

Neste caso, estamos selecionando a camada base `python:3.8-alpine` (veja [Dockerfile para python3.8/alpine3.12](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile)) pois ela já possui a versão do python e pip que precisamos para executar nosso aplicativo.

A versão `alpine` significa que ela usa a distribuição [Alpine Linux](https://en.wikipedia.org/wiki/Alpine_Linux), que é significativamente menor do que muitas outras versões de Linux, com cerca de 8 MB de tamanho, enquanto uma instalação mínima em disco pode ter cerca de 130 MB. Uma imagem menor significa que ela fará o download (implantação) muito mais rápido, e também tem vantagens para a segurança porque tem uma superfície de ataque menor. [Alpine Linux](https://alpinelinux.org/downloads/) é uma distribuição Linux baseada em musl e BusyBox.

Aqui estamos usando a tag "3.8-alpine" para a imagem python. Dê uma olhada nas tags disponíveis para a imagem python oficial no [Docker Hub](https://hub.docker.com/_/python/). É uma boa prática usar uma tag específica ao herdar uma imagem pai para que as alterações na dependência pai sejam controladas. Se nenhuma tag for especificada, a tag "latest" entra em vigor, que atua como um ponteiro dinâmico que aponta para a versão mais recente de uma imagem.

Por razões de segurança, é muito importante entender as camadas sobre as quais você constrói sua imagem docker. Por essa razão, é altamente recomendável usar apenas imagens "oficiais" encontradas no [docker hub](https://hub.docker.com/) ou imagens não comunitárias encontradas no docker-store. Essas imagens são [vetted](https://docs.docker.com/docker-hub/official_repos/) para atender a certos requisitos de segurança e também possuem uma documentação muito boa para os usuários seguirem. Você pode encontrar mais informações sobre esta [imagem base python](https://hub.docker.com/), bem como todas as outras imagens que você pode usar, no [docker hub](https://hub.docker.com).

Para um aplicativo mais complexo, você pode precisar usar uma imagem `FROM` que esteja mais acima na cadeia. Por exemplo, o [Dockerfile](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) pai para nosso aplicativo python começa com `FROM alpine`, então especifica uma série de comandos `CMD` e `RUN` para a imagem. Se você precisasse de um controle mais preciso, poderia começar com `FROM alpine` (ou uma distribuição diferente) e executar essas etapas você mesmo. Para começar, no entanto, recomendo usar uma imagem oficial que corresponda de perto às suas necessidades.

**RUN pip install flask**
O comando `RUN` executa comandos necessários para configurar sua imagem para seu aplicativo, como instalar pacotes, editar arquivos ou alterar permissões de arquivos. Neste caso, estamos instalando flask. Os comandos `RUN` são executados no momento da construção e são adicionados às camadas de sua imagem.

**CMD ["python","app.py"]**
`CMD` é o comando que é executado quando você inicia um container. Aqui estamos usando `CMD` para executar nosso aplicativo python.

Pode haver apenas um `CMD` por Dockerfile. Se você especificar mais de um `CMD`, o último `CMD` entrará em vigor. O python:3.8-alpine pai também especifica um `CMD` (`CMD python3`). Você pode encontrar o Dockerfile para a imagem python:alpine oficial [aqui](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile).

Você pode usar a imagem python oficial diretamente para executar scripts python sem instalar python em seu host. Mas hoje, estamos criando uma imagem personalizada para incluir nossa fonte, para que possamos construir uma imagem com nosso aplicativo e enviá-la para outros ambientes.

**COPY app.py /app.py**
Isso copia o app.py no diretório local (onde você executará `docker image build`) em uma nova camada da imagem. Esta instrução é a última linha no Dockerfile. Camadas que mudam com frequência, como copiar o código-fonte na imagem, devem ser colocadas na parte inferior do arquivo para aproveitar ao máximo o cache de camadas do Docker. Isso nos permite evitar a reconstrução de camadas que, de outra forma, poderiam ser armazenadas em cache. Por exemplo, se houvesse uma alteração na instrução `FROM`, ela invalidaria o cache para todas as camadas subsequentes desta imagem. Demonstraremos isso um pouco mais tarde neste laboratório.

Parece contraintuitivo colocar isso após a linha `CMD ["python","app.py"]`. Lembre-se, a linha `CMD` é executada apenas quando o container é iniciado, então não receberemos um erro `file not found` aqui.

E pronto: um Dockerfile muito simples. Uma lista completa de comandos que você pode colocar em um Dockerfile pode ser encontrada [aqui](https://docs.docker.com/engine/reference/builder/). Agora que definimos nosso Dockerfile, vamos usá-lo para construir nossa imagem docker personalizada.

Construa a imagem docker.

Passe `-t` para nomear sua imagem `python-hello-world`.

```bash
docker image build -t python-hello-world .
```

Verifique se sua imagem aparece em sua lista de imagens.

```bash
docker image ls
```

**Observe** que sua imagem base `python:3.8-alpine` também está em sua lista.

Você pode executar um comando de histórico para mostrar o histórico de uma imagem e suas camadas,

```bash
docker history python-hello-world
docker history python:3.8-alpine
```
