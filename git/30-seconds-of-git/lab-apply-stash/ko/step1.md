# Stash 적용하기

`git-playground` 저장소의 feature 브랜치에서 작업 중이며, 버그 수정을 위해 다른 브랜치로 전환해야 합니다. 하지만 아직 커밋할 준비가 되지 않은 변경 사항이 있습니다. 이러한 변경 사항을 저장하고 다른 브랜치로 전환하려고 합니다. 버그 수정을 완료한 후에는 stash 를 적용하고 feature 브랜치에서 작업을 계속하고 싶습니다.

변경 사항은 `feature-branch` 브랜치에 stash 되었으며, stash 메시지는 "my changes"입니다.

1. `git-playground` 디렉토리로 이동합니다:

```shell
cd git-playground
```

2. `master` 브랜치로 전환하고 버그를 수정한 후 stash 합니다. stash 메시지는 "fix the bug"입니다. `file1.txt` 파일의 내용을 "hello,world"로 업데이트하여 버그를 수정합니다:

```shell
git checkout master
echo "hello,world" > file1.txt
git stash save "fix the bug"
```

3. `feature-branch` 브랜치로 전환하고, stash 목록을 확인한 다음, 정보가 "my changes"인 stash 를 적용합니다:

```shell
git checkout feature-branch
git stash apply stash@{1}
```

다음은 `README.md` 파일의 내용입니다:

```
# git-playground
Git Playground
some changes
```

stash 하기 전에 했던 변경 사항이 이제 적용된 것을 확인할 수 있습니다.
