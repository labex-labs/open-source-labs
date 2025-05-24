# Enviar para um Registro Central

Navegue até [Docker Hub](https://hub.docker.com) e crie uma conta, caso ainda não tenha uma. Alternativamente, você também pode usar [https://quay.io](https://quay.io), por exemplo.

Para este laboratório, usaremos o Docker Hub como nosso registro central. O Docker Hub é um serviço gratuito para armazenar imagens publicamente disponíveis, ou você pode pagar para armazenar imagens privadas. Vá para o site [Docker Hub](https://hub.docker.com) e crie uma conta gratuita.

A maioria das organizações que usam o docker intensamente configurará seu próprio registro internamente. Para simplificar as coisas, usaremos o Docker Hub, mas os seguintes conceitos se aplicam a qualquer registro.

Login

Você pode fazer login na conta do registro de imagens digitando `docker login` em seu terminal, ou se estiver usando podman, digite `podman login`.

```bash
labex:project/ $ export DOCKERHUB_USERNAME=<your_docker_username>
labex:project/ $ docker login docker.io -u $DOCKERHUB_USERNAME
Password:
WARNING! Your password will be stored unencrypted in /home/labex/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

Marque sua imagem com seu nome de usuário

A convenção de nomenclatura do Docker Hub é marcar sua imagem com [nome de usuário do dockerhub]/[nome da imagem]. Para fazer isso, vamos marcar nossa imagem criada anteriormente `python-hello-world` para se adequar a esse formato.

```bash
docker tag python-hello-world $DOCKERHUB_USERNAME/python-hello-world
```

Envie sua imagem para o registro

Depois de termos uma imagem devidamente marcada, podemos usar o comando `docker push` para enviar nossa imagem para o registro do Docker Hub.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

Verifique sua imagem no docker hub em seu navegador

Navegue até [Docker Hub](https://hub.docker.com) e vá para seu perfil para ver sua imagem recém-carregada em `https://hub.docker.com/repository/docker/<dockerhub-username>/python-hello-world`.

Agora que sua imagem está no Docker Hub, outros desenvolvedores e operações podem usar o comando `docker pull` para implantar sua imagem em outros ambientes.

**Observação:** As imagens Docker contêm todas as dependências de que precisam para executar um aplicativo dentro da imagem. Isso é útil porque não precisamos mais lidar com a deriva do ambiente (diferenças de versão) quando confiamos em dependências que são instaladas em todos os ambientes em que implantamos. Também não precisamos passar por etapas adicionais para provisionar esses ambientes. Apenas uma etapa: instale o docker e você está pronto para começar.
