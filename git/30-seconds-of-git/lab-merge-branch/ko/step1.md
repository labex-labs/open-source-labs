# 브랜치 병합

Git 을 사용하여 브랜치를 현재 브랜치에 병합하는 것이 과제입니다. 대상 브랜치로 전환한 다음 소스 브랜치를 병합해야 합니다. 이는 `feature-branch-A` 브랜치의 변경 사항을 프로젝트의 `master` 브랜치에 결합하려는 경우 유용할 수 있습니다.

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. 다음 단계를 따라 `feature-branch-A`를 `master` 브랜치에 병합하십시오.

1. 저장소를 복제하고, 디렉토리로 이동하여 ID 를 구성합니다.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `feature-branch-A` 브랜치를 생성합니다. 해당 브랜치로 전환합니다.

```shell
git checkout -b feature-branch-A
```

3. "hello,world"를 `file2.txt` 파일에 추가하고, 스테이징 영역에 추가한 다음 "fix file2.txt" 메시지로 커밋합니다.

```shell
echo "hello,world" >> file2.txt
git add .
git commit -m "fix file2.txt"
```

4. `master` 브랜치로 전환합니다.

```shell
git checkout master
```

5. `feature-branch-A`를 `master` 브랜치에 병합합니다.

```shell
git merge feature-branch-A
```

6. 병합 과정에서 발생할 수 있는 모든 충돌을 해결합니다.

다음은 `git log`를 실행한 결과입니다.

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
