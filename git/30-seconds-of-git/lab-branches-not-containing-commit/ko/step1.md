# 커밋을 포함하지 않는 브랜치 찾기

여러 브랜치로 작업하는 프로젝트에서 특정 커밋을 포함하지 않는 모든 브랜치를 찾아야 합니다. 이는 특정 변경 사항이 모든 브랜치에 적용되었는지 확인하거나, 어떤 브랜치가 오래되어 업데이트가 필요한지 알고 싶을 때 유용할 수 있습니다.

이 랩에서는 `https://github.com/your-username/git-playground`라는 Git 저장소를 사용합니다.

1. 다음 명령을 사용하여 이 저장소를 로컬 머신에 복제합니다.

```shell
git clone https://github.com/your-username/git-playground.git
```

2. 저장소를 복제한 후 다음 명령을 사용하여 디렉토리로 이동하고 ID 를 구성합니다.

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `new-branch` 브랜치를 생성하고 전환한 다음 해당 브랜치에서 일부 코드 변경을 수행한 후 커밋합니다. 커밋 메시지는 "Create a new-branch branch"입니다.

```shell
git checkout -b new-branch
echo "hello,world" > file1.txt
git commit -am "Create a new-branch branch"
```

4. 커밋 메시지 "Create a new-branch branch"의 해시를 확인합니다.

```shell
git log
```

5. 커밋 메시지가 "Create a new-branch branch"인 해시를 포함하지 않는 모든 브랜치를 찾습니다. 이를 위해 다음 명령을 사용할 수 있습니다.

```shell
git branch --no-contains 31c5ac20129151af1
```

이렇게 하면 지정된 커밋을 포함하지 않는 모든 브랜치의 목록이 출력됩니다. 이 경우 출력은 다음과 같습니다.

```shell
master
```

이는 `master` 브랜치가 해시 `31c5ac20129151af1`의 커밋을 포함하지 않음을 의미합니다.
