# 중앙 레지스트리에 푸시

[Docker Hub](https://hub.docker.com)로 이동하여 아직 계정이 없다면 계정을 만듭니다. 또는 [https://quay.io](https://quay.io)를 사용할 수도 있습니다.

이 랩에서는 Docker Hub 를 중앙 레지스트리로 사용합니다. Docker Hub 는 공개적으로 사용 가능한 Image 를 저장하는 무료 서비스이며, 유료로 개인 Image 를 저장할 수도 있습니다. [Docker Hub](https://hub.docker.com) 웹사이트로 이동하여 무료 계정을 만듭니다.

Docker 를 많이 사용하는 대부분의 조직은 자체 레지스트리를 내부적으로 설정합니다. 간소화를 위해 Docker Hub 를 사용하지만, 다음 개념은 모든 레지스트리에 적용됩니다.

로그인

터미널에서 `docker login`을 입력하거나, podman 을 사용하는 경우 `podman login`을 입력하여 Image 레지스트리 계정에 로그인할 수 있습니다.

```bash
labex:project/ $ export DOCKERHUB_USERNAME=<your_docker_username>
labex:project/ $ docker login docker.io -u $DOCKERHUB_USERNAME
Password:
WARNING! Your password will be stored unencrypted in /home/labex/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

사용자 이름으로 Image 태그 지정

Docker Hub 명명 규칙은 [dockerhub username]/[image name]으로 Image 에 태그를 지정하는 것입니다. 이를 위해 이전에 생성한 Image `python-hello-world`에 해당 형식에 맞게 태그를 지정합니다.

```bash
docker tag python-hello-world $DOCKERHUB_USERNAME/python-hello-world
```

Image 를 레지스트리에 푸시

적절하게 태그가 지정된 Image 가 있으면 `docker push` 명령을 사용하여 Image 를 Docker Hub 레지스트리에 푸시할 수 있습니다.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

브라우저에서 Docker Hub 에서 Image 확인

[Docker Hub](https://hub.docker.com)로 이동하여 프로필로 이동하여 새로 업로드된 Image 를 `https://hub.docker.com/repository/docker/<dockerhub-username>/python-hello-world`에서 확인합니다.

이제 Image 가 Docker Hub 에 있으므로 다른 개발자와 운영자는 `docker pull` 명령을 사용하여 Image 를 다른 환경에 배포할 수 있습니다.

**참고:** Docker Image 에는 Image 내에서 애플리케이션을 실행하는 데 필요한 모든 종속성이 포함되어 있습니다. 이는 모든 배포 환경에 설치된 종속성에 의존할 때 환경 드리프트 (버전 차이) 를 더 이상 처리할 필요가 없기 때문에 유용합니다. 또한 이러한 환경을 프로비저닝하기 위한 추가 단계를 거칠 필요가 없습니다. 단 한 단계: Docker 를 설치하면 됩니다.
