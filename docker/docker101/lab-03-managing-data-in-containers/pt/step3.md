# [Opcional] OverlayFS

OverlayFS é uma implementação de `sistema de arquivos de montagem de união` (union mount filesystem) para Linux. Para entender o que é um volume Docker, é útil entender como as camadas e o sistema de arquivos funcionam no Docker.

Para iniciar um container, o Docker pega a imagem somente leitura e cria uma nova camada de leitura-gravação por cima. Para visualizar as camadas como uma só, o Docker usa um Sistema de Arquivos de União ou OverlayFS (Overlay File System), especificamente o driver de armazenamento `overlay2`.

Para ver os arquivos gerenciados pelo host Docker, você precisa de acesso ao sistema de arquivos do processo Docker. Usando as flags `--privileged` e `--pid=host`, você pode acessar o namespace de ID do processo do host de dentro de um container como `busybox`. Você pode então navegar para o diretório `/var/lib/docker/overlay2` do Docker para ver as camadas baixadas que são gerenciadas pelo Docker.

Para visualizar a lista atual de camadas no Docker:

```bash
$ docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh

/ # ls -l /var/lib/docker/overlay2
total 16
drwx------ 3 root root 4096 Sep 25 19:44 0e55ecaa4d17c353191e68022d9a17fde64fb5e9217b07b5c56eb4c74dad5b32
drwx------ 5 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d
drwx------ 4 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d-init
drwx------ 2 root root 4096 Sep 25 19:44 l

/ # exit
```

Faça o pull da imagem `ubuntu` e verifique novamente:

```bash
docker pull ubuntu
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
```

Digite o comando para ver a lista de camadas novamente:

```
ls -l /var/lib/docker/overlay2/ & exit
```

Você vê que, ao baixar a imagem `ubuntu`, implicitamente foram baixadas 4 novas camadas:

- a611792b4cac502995fa88a888261dfba0b5d852e72f9db9e075050991423779
- d181f1a41fc35a45c16e8bfcb8eee6f768f3b98f82210a43ea65f284a45fcd65
- dac2f37f6280a076836d39b87b0ae5ebf5c0d386b6d8b991b103aadbcebaa7c6
- f3e921b440c37c86d06cd9c9fb70df50edad553c36cc87f84d5eeba734aae709

O driver de armazenamento `overlay2` essencialmente sobrepõe diferentes diretórios no host e os apresenta como um único diretório.

- camada base ou lowerdir,
- camada `diff` ou upperdir,
- camada overlay (visão do usuário), e
- diretório `work`.

OverlayFS se refere aos diretórios inferiores como `lowerdir`, que contém a imagem base e as camadas somente leitura (R/O) que são baixadas.

O diretório superior é chamado de `upperdir` e é a camada de container de leitura-gravação (R/W).

A visão unificada ou camada `overlay` é chamada de `merged`.

Finalmente, um `workdir` é necessário, que é um diretório vazio usado pelo overlay para uso interno.

O driver `overlay2` suporta até 128 camadas OverlayFS inferiores. O diretório `l` contém identificadores de camada abreviados como links simbólicos.

![Overlay2 Storage Driver](../assets/overlay2-driver.png)

Limpeza:

```bash
docker system prune -a
clear
```
