# Compreendendo as Camadas da Imagem

Uma das principais propriedades de design do Docker é o uso do sistema de arquivos de união (union file system).

Considere o `Dockerfile` que criamos anteriormente:

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py
```

Cada uma dessas linhas é uma camada. Cada camada contém apenas o delta, a diferença ou as alterações das camadas anteriores. Para juntar essas camadas em um único contêiner em execução, o Docker utiliza o `union file system` para sobrepor as camadas de forma transparente em uma única visualização.

Cada camada da imagem é `read-only` (somente leitura), exceto a camada superior, que é criada para o contêiner em execução. A camada de contêiner de leitura/gravação implementa "copy-on-write" (cópia sob escrita), o que significa que os arquivos armazenados nas camadas inferiores da imagem são puxados para a camada de contêiner de leitura/gravação somente quando edições são feitas nesses arquivos. Essas alterações são então armazenadas na camada do contêiner em execução. A função "copy-on-write" é muito rápida e, em quase todos os casos, não tem um efeito perceptível no desempenho. Você pode inspecionar quais arquivos foram puxados para o nível do contêiner com o comando `docker diff`. Mais informações sobre como usar `docker diff` podem ser encontradas [aqui](https://docs.docker.com/engine/reference/commandline/diff/).

![understanding image layers](../assets/lab2_understanding_image_layers_1.png)

Como as camadas da imagem são `read-only`, elas podem ser compartilhadas por imagens e por contêineres em execução. Por exemplo, a criação de um novo aplicativo python com seu próprio Dockerfile com camadas base semelhantes, compartilharia todas as camadas que tinha em comum com o primeiro aplicativo python.

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app2.py"]
COPY app2.py /app2.py
```

![understanding image layers](../assets/lab2_understanding_image_layers_2.png)

Você também pode experimentar o compartilhamento de camadas ao iniciar vários contêineres a partir da mesma imagem. Como os contêineres usam as mesmas camadas somente leitura, você pode imaginar que iniciar contêineres é muito rápido e tem uma pegada muito baixa no host.

Você pode notar que existem linhas duplicadas neste Dockerfile e no Dockerfile que você criou anteriormente neste laboratório. Embora este seja um exemplo muito trivial, você pode puxar linhas comuns de ambos os Dockerfiles para um Dockerfile "base", ao qual você pode apontar com cada um de seus Dockerfiles filhos usando o comando `FROM`.

O image layering (camadas de imagem) permite o mecanismo de cache do docker para builds e pushes. Por exemplo, a saída do seu último `docker push` mostra que algumas das camadas da sua imagem já existem no Docker Hub.

```bash
$ docker push $DOCKERHUB_USERNAME/python-hello-world
```

Para olhar mais de perto as camadas, você pode usar o comando `docker image history` da imagem python que criamos.

```bash
$ docker image history python-hello-world
```

Cada linha representa uma camada da imagem. Você notará que as linhas superiores correspondem ao seu Dockerfile que você criou, e as linhas abaixo são puxadas da imagem python pai. Não se preocupe com as tags "\<missing\>". Estas ainda são camadas normais; elas simplesmente não receberam um ID pelo sistema docker.
