# 바인드 마운트 (Bind Mounts)

`mount` 구문은 `volume` 구문보다 Docker 에서 권장됩니다. 바인드 마운트는 볼륨에 비해 기능이 제한적입니다. 파일 또는 디렉토리는 컨테이너에 마운트될 때 호스트 머신에서 전체 경로로 참조됩니다. 바인드 마운트는 호스트 머신의 파일 시스템에 특정 디렉토리 구조가 있어야 하며 Docker CLI 를 사용하여 바인드 마운트를 관리할 수 없습니다. 바인드 마운트는 컨테이너에서 실행되는 프로세스를 통해 호스트 파일 시스템을 변경할 수 있습니다.

콜론 구분자 (:) 로 구분된 세 개의 필드를 사용하는 `-v` 구문 대신, `mount` 구문은 더 자세하며 여러 `key-value` 쌍을 사용합니다.

- type: bind, volume 또는 tmpfs,
- source: 호스트 머신의 파일 또는 디렉토리 경로,
- destination: 컨테이너 내 경로,
- readonly,
- bind-propagation: rprivate, private, rshared, shared, rslave, slave,
- consistency: consistent, delegated, cached,
- mount.

```bash
cd /home/labex/project
mkdir data
docker run -it --name busybox --mount type=bind,source="$(pwd)"/data,target=/data busybox sh
```

컨테이너에서 명령을 입력합니다.

```
echo "hello busybox" > /data/hi.txt
exit
```

파일이 호스트 머신에 생성되었는지 확인합니다.

```
cat data/hi.txt
```
