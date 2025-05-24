# Git 사용자 정보 구성

새로운 프로젝트를 시작하여 Git 에 대한 사용자 정보를 구성하려고 합니다. 리포지토리에 적용하는 모든 변경 사항에 이름과 이메일 주소가 연결되도록 하려고 합니다.

이 랩에서는 `https://github.com/labex-labs/git-playground`라는 Git 리포지토리를 사용합니다. 이 리포지토리에 대한 사용자 정보를 구성하려면 다음 단계를 따르세요.

1. 다음 명령을 사용하여 리포지토리를 복제 (clone) 합니다.

```
git clone https://github.com/labex-labs/git-playground.git
```

2. 다음 명령을 사용하여 복제된 리포지토리로 이동합니다.

```
cd git-playground
```

3. `git config` 명령을 사용하여 리포지토리에 대한 사용자 정보를 설정합니다. 예를 들어, 이메일 주소가 `jane.doe@example.com`이고 이름이 `Jane Doe`인 경우 다음 명령을 사용합니다.

```
git config user.email "jane.doe@example.com"
git config user.name "Jane Doe"
```

4. 다음 명령을 사용하여 사용자 정보가 올바르게 설정되었는지 확인합니다: `git config --list`. `user.email` 및 `user.name` 키 아래에 이메일 주소와 이름이 표시되어야 합니다.

랩을 완료한 후의 결과는 다음과 같습니다.

![Git user configuration result](../assets/challenge-config-user-step1-1.png)
