# 업스트림 브랜치 생성 자동화

개발자로서, 원격 저장소에서 브랜치를 수동으로 생성하는 번거로움을 피하기 위해 푸시 시 업스트림 브랜치 생성 프로세스를 자동화하고자 합니다.

이 랩에서는 `https://github.com/labex-labs/git-playground` 저장소를 계정으로 포크하고, 계정의 `git-playground` 저장소를 사용하여 푸시 시 자동으로 업스트림 브랜치를 생성합니다.

1. GitHub 웹사이트에서 계정에 로그인하고 `https://github.com/labex-labs/git-playground`를 찾아 저장소를 계정으로 포크합니다.
2. 포크한 저장소 페이지에서 `Code` 버튼을 클릭하고 저장소의 URL 을 복사합니다.
3. 저장소를 클론하고, 디렉토리로 이동하여 ID 를 구성합니다.

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

4. 다음 명령을 사용하여 푸시 시 자동 업스트림 브랜치 생성을 활성화합니다.

```shell
git config --global push.default current
```

5. 원격 저장소에 존재하지 않는 `new-feature`라는 새 브랜치를 푸시합니다.

```shell
git checkout -b new-feature
git push
```

6. 새 브랜치가 원격 저장소에 생성되었는지 확인합니다.

```shell
git ls-remote --heads origin
```

다음은 랩을 완료한 후의 결과입니다.

![자동 업스트림 브랜치 결과](../assets/challenge-automatic-push-upstream-step1-1.png)
