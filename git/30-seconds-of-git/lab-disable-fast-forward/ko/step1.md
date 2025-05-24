# 빠른 병합 비활성화

기본적으로 Git 은 분기된 커밋이 없는 브랜치를 병합하기 위해 빠른 병합 (fast forward merging) 을 사용합니다. 이는 새로운 커밋이 없는 브랜치가 있는 경우, Git 이 병합하려는 브랜치의 포인터를 병합하려는 브랜치의 최신 커밋으로 단순히 이동시킨다는 것을 의미합니다. 이는 몇몇 경우에 유용할 수 있지만, 특히 여러 기여자가 참여하는 대규모 프로젝트에서 문제를 일으킬 수 있습니다. 예를 들어, 두 명의 개발자가 동일한 브랜치에서 작업하고 둘 다 변경 사항을 적용하는 경우, 빠른 병합은 해결하기 어려운 충돌을 발생시킬 수 있습니다.

빠른 병합을 비활성화하기 위해 `https://github.com/labex-labs/git-playground`에서 제공하는 저장소를 사용해 보겠습니다.

1. 저장소를 복제하고, 디렉토리로 이동한 후, 신원을 구성합니다.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `my-branch`라는 브랜치를 생성하고 전환한 다음, `hello.txt` 파일을 생성하고 "hello,world"를 추가하고, 스테이징 영역에 추가하고 "Added hello.txt" 메시지로 커밋합니다.

```shell
git checkout -b my-branch
echo "hello,world" > hello.txt
git add .
git commit -m "Added hello.txt"
```

3. 빠른 병합을 비활성화하려면 다음 명령을 실행합니다.

```shell
git config --add merge.ff false
```

이렇게 하면 가능한 경우에도 모든 브랜치에 대해 빠른 병합이 비활성화됩니다. `--global` 플래그를 사용하여 이 옵션을 전역적으로 구성할 수 있습니다.

```shell
git config --global --add merge.ff false
```

4. `master` 브랜치로 다시 전환하고 `my-branch` 브랜치를 병합한 다음, 텍스트를 변경하지 않고 저장하고 종료합니다.

```shell
git checkout master
git merge my-branch
```

이제 Git 은 빠른 병합이 가능하더라도 항상 병합 커밋을 생성합니다.

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch 'my-branch'
```
