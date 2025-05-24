# 원격 저장소에서 최신 변경 사항 가져오기 (Pull)

여러 명의 개발자와 함께 프로젝트를 진행하고 있으며, 팀원들이 수행한 최신 변경 사항으로 코드베이스의 로컬 복사본이 최신 상태인지 확인해야 합니다. 이를 위해 원격 저장소에서 최신 변경 사항을 가져와야 합니다.

이 랩에서는 `https://github.com/labex-labs/git-playground`라는 Git 저장소를 사용합니다. 랩을 완료하려면 아래 단계를 따르세요.

1. 복제된 저장소의 디렉토리로 이동합니다.

```shell
cd git-playground
```

2. 원격 저장소의 `master` 브랜치에서 최신 변경 사항을 가져옵니다.

```shell
git pull origin master
```

`git pull` 명령을 실행한 후, 저장소의 로컬 복사본이 원격 저장소와 최신 상태임을 나타내는 메시지가 표시되어야 합니다.

다음은 pull 후의 결과입니다.

![git pull command output](../assets/challenge-pull-changes-step1-1.png)
