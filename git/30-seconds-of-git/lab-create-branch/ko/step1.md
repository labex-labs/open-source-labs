# 새로운 브랜치 생성

이 랩 (lab) 을 위해, `https://github.com/labex-labs/git-playground`라는 Git 저장소를 GitHub 계정으로 포크 (fork) 합니다. `https://github.com/your-username/git-playground`라는 Git 저장소에서 프로젝트를 작업하고 있습니다. 새로운 기능을 작업하기 위해 `feature-1`이라는 새로운 브랜치를 생성해야 합니다.

1. 저장소를 클론 (clone) 하고, 디렉토리로 이동하여 ID 를 구성합니다:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. 현재 브랜치를 확인합니다:

```shell
git branch
```

3. `feature-1`이라는 새로운 브랜치를 생성합니다:

```shell
git checkout -b feature-1
```

4. 현재 `feature-1` 브랜치에 있는지 확인합니다:

```shell
git branch
```

5. 변경 사항을 원격 저장소 (remote repository) 로 푸시 (push) 합니다:

```shell
git push -u origin feature-1
```

`git branch -r` 명령을 실행하면 다음과 같은 결과가 나타납니다:

![git branch remote output](../assets/challenge-create-branch-step1-1.png)
