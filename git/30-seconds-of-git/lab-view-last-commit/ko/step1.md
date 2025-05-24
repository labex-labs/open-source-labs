# 마지막 커밋 보기

여러 명의 개발자와 함께 프로젝트를 진행 중이며, 프로젝트의 Git 저장소에 마지막으로 커밋된 내용을 확인해야 합니다. 커밋 메시지, 작성자, 날짜를 포함한 커밋의 세부 정보를 확인하고 싶습니다.

Git 저장소에 마지막으로 커밋된 내용을 보려면 다음 단계를 따르세요.

1. 컴퓨터에서 터미널을 엽니다.
2. Git 저장소가 있는 디렉토리로 이동합니다.

```shell
cd git-playground
```

3. 마지막 커밋을 봅니다.

```shell
git log -1
```

출력 결과는 커밋 메시지, 작성자, 날짜를 포함한 마지막 커밋의 세부 정보를 보여줍니다.

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
