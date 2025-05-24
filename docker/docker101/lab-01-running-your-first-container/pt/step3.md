# Executar Vários Contêineres

## Explorar o Docker Hub

O [Docker Hub](https://hub.docker.com/explore/) é o registro central público para imagens Docker, que contém imagens da comunidade e oficiais.

Ao pesquisar imagens, você encontrará filtros para imagens "Docker Certified", "Verified Publisher" e "Official Images". Selecione o filtro "Docker Certified" para encontrar imagens que são consideradas prontas para empresas e são testadas com o produto Docker Enterprise Edition. É importante evitar o uso de conteúdo não verificado da Docker Store ao desenvolver suas próprias imagens que se destinam a serem implantadas no ambiente de produção. Essas imagens não verificadas podem conter vulnerabilidades de segurança ou possivelmente até mesmo software malicioso.

Na etapa 2 deste laboratório, iniciaremos alguns contêineres usando algumas imagens verificadas do Docker Hub: servidor web nginx e banco de dados mongo.

## Executar um Servidor Nginx

Vamos executar um contêiner usando a [imagem Nginx oficial](https://hub.docker.com/_/nginx) do Docker Hub.

```bash
docker container run --detach --publish 8080:80 --name nginx nginx
```

Estamos usando algumas novas flags aqui. A flag `--detach` executará este contêiner em segundo plano. A flag `publish` publica a porta 80 no contêiner (a porta padrão para nginx), através da porta 8080 em nosso host. Lembre-se de que o namespace NET dá aos processos do contêiner sua própria pilha de rede. A flag `--publish` é um recurso que nos permite expor a rede através do contêiner para o host.

Como você sabe que a porta 80 é a porta padrão para nginx? Porque ela está listada na [documentação](https://hub.docker.com/_/nginx) no Docker Hub. Em geral, a documentação para as imagens verificadas é muito boa, e você vai querer consultá-las ao executar contêineres usando essas imagens.

Também estamos especificando a flag `--name`, que nomeia o contêiner. Cada contêiner tem um nome, se você não especificar um, o Docker atribuirá um aleatoriamente para você. Especificar seu próprio nome facilita a execução de comandos subsequentes em seu contêiner, pois você pode referenciar o nome em vez do ID do contêiner. Por exemplo: `docker container inspect nginx` em vez de `docker container inspect 5e1`.

Como esta é a primeira vez que você está executando o contêiner nginx, ele baixará a imagem nginx da Docker Store. Contêineres subsequentes criados a partir da imagem Nginx usarão a imagem existente localizada em seu host.

Nginx é um servidor web leve. Você pode acessar o servidor nginx na aba **Web 8080** da VM do LabEx. Alterne-a e atualize a página para ver a saída do nginx.

![step 2 nginx](../assets/20230829-11-16-04-BazUogDa.png)

## Executar um Servidor de Banco de Dados `mongo`

Agora, execute um servidor mongoDB. Usaremos a [imagem mongoDB oficial](https://hub.docker.com/_/mongo) do Docker Hub. Em vez de usar a tag `latest` (que é a padrão se nenhuma tag for especificada), usaremos uma versão específica da imagem mongo: 4.4.

```bash
docker container run --detach --publish 8081:27017 --name mongo mongo:4.4
```

Novamente, como esta é a primeira vez que estamos executando um contêiner mongo, baixaremos a imagem mongo da Docker Store. Estamos usando a flag `--publish` para expor a porta 27017 mongo em nosso host. Temos que usar uma porta diferente de 8080 para o mapeamento do host, pois essa porta já está exposta em nosso host. Novamente, consulte os [documentos oficiais](https://hub.docker.com/_/mongo) no Docker Hub para obter mais detalhes sobre como usar a imagem mongo.

Veja a saída do mongoDB usando `0.0.0.0:8081` no navegador da Web. Você deve ver uma mensagem que retornará um aviso do MongoDB.

![MongoDB server output warning](../assets/20230829-11-19-23-PkodKK48.png)

Verifique seus contêineres em execução com `docker container ls`

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon ..." Less than a second ago Up 2 seconds 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 17 seconds ago Up 19 seconds 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 5 minutes ago Up 5 minutes priceless_kepler
```

Você deve ver que tem um contêiner de servidor web Nginx e um contêiner MongoDB em execução em seu host. Observe que não configuramos esses contêineres para se comunicarem entre si.

Você pode ver os nomes "nginx" e "mongo" que demos aos nossos contêineres e o nome aleatório (no meu caso "priceless_kepler") que foi gerado para o contêiner ubuntu. Você também pode ver os mapeamentos de porta que especificamos com a flag `--publish`. Para obter mais informações sobre esses contêineres em execução, você pode usar o comando `docker container inspect [container id`.

Uma coisa que você pode notar é que o contêiner mongo está executando o comando `docker-entrypoint`. Este é o nome do executável que é executado quando o contêiner é iniciado. A imagem mongo requer alguma configuração prévia antes de iniciar o processo do banco de dados. Você pode ver exatamente o que o script faz olhando para ele no [github](https://github.com/docker-library/mongo). Normalmente, você pode encontrar o link para a fonte do github na página de descrição da imagem no site da Docker Store.

Os contêineres são autossuficientes e isolados, o que significa que podemos evitar possíveis conflitos entre contêineres com diferentes dependências de sistema ou tempo de execução. Por exemplo: implantar um aplicativo que usa Java 7 e outro aplicativo que usa Java 8 no mesmo host. Ou executar vários contêineres nginx que todos têm a porta 80 como suas portas de escuta padrão (se expostas no host usando a flag `--publish`, as portas selecionadas para o host precisarão ser exclusivas). Os benefícios do isolamento são possíveis por causa dos Namespaces Linux.

**Observação**: Você não precisou instalar nada em seu host (além do Docker) para executar esses processos! Cada contêiner inclui as dependências de que precisa dentro do contêiner, então você não precisa instalar nada em seu host diretamente.

Executar vários contêineres no mesmo host nos dá a capacidade de utilizar totalmente os recursos (cpu, memória, etc.) disponíveis em um único host. Isso pode resultar em enormes economias de custos para uma empresa.

Embora a execução de imagens diretamente do Docker Hub possa ser útil às vezes, é mais útil criar imagens personalizadas e consultar as imagens oficiais como ponto de partida para essas imagens. Mergulharemos na construção de nossas próprias imagens personalizadas no Lab 2.
