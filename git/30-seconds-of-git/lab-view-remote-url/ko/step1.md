# 원격 URL 보기

개발자로서 Git 구성을 문제 해결하거나 올바른 저장소로 작업하고 있는지 확인하는 등 다양한 이유로 원격 저장소의 URL 을 확인해야 할 수 있습니다. 그러나 Git 명령에 익숙하지 않은 경우 원격 URL 을 확인하는 방법을 아는 것이 어려울 수 있습니다.

이 랩에서는 `https://github.com/labex-labs/git-playground`라는 Git 저장소를 사용합니다. 이 저장소의 원격 URL 을 보려면 다음 단계를 따르세요.

1. 터미널 또는 명령 프롬프트를 엽니다.
2. `git-playground` 저장소를 복제한 디렉토리로 이동합니다.

```shell
cd git-playground
```

3. 다음 명령을 실행하여 원격 URL 을 확인합니다.

```shell
git config --get remote.origin.url
```

출력 결과는 원격 저장소의 URL 을 표시해야 하며, 이 경우 `https://github.com/labex-labs/git-playground.git`입니다.
