# Bind Mounts

A sintaxe `mount` é recomendada pelo Docker em vez da sintaxe `volume`. Bind mounts têm funcionalidade limitada em comparação com volumes. Um arquivo ou diretório é referenciado por seu caminho completo na máquina host quando montado em um container. Bind mounts dependem do sistema de arquivos da máquina host ter uma estrutura de diretórios específica disponível e você não pode usar a CLI do Docker para gerenciar bind mounts. Observe que bind mounts podem alterar o sistema de arquivos host por meio de processos em execução em um container.

Em vez de usar a sintaxe `-v` com três campos separados por dois pontos (:), a sintaxe `mount` é mais verbosa e usa vários pares `chave-valor`:

- type: bind, volume ou tmpfs,
- source: caminho para o arquivo ou diretório na máquina host,
- destination: caminho no container,
- readonly,
- bind-propagation: rprivate, private, rshared, shared, rslave, slave,
- consistency: consistent, delegated, cached,
- mount.

```bash
cd /home/labex/project
mkdir data
docker run -it --name busybox --mount type=bind,source="$(pwd)"/data,target=/data busybox sh
```

Digite o comando no container:

```
echo "hello busybox" > /data/hi.txt
exit
```

Verifique se o arquivo foi criado na máquina host.

```
cat data/hi.txt
```
