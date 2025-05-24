# 다른 브랜치에 리베이스하기

개발자로서, 여러 브랜치가 있는 프로젝트에서 작업하고 있다고 가정해 봅시다. 여러분은 자신의 브랜치에 변경 사항을 적용했고, 해당 변경 사항을 다른 브랜치에 통합하고 싶습니다. 하지만 깔끔하고 선형적인 히스토리를 유지하고 싶기 때문에 브랜치를 병합 (merge) 하고 싶지 않습니다. 이 경우, `git rebase` 명령을 사용하여 브랜치를 다른 브랜치에 리베이스할 수 있습니다.

이 랩 (lab) 에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다. 랩을 완료하려면 아래 단계를 따르세요.

1. 저장소를 복제하고, 디렉토리로 이동한 후, 신원을 구성합니다.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `one-branch`라는 브랜치를 생성하고 전환합니다.

```shell
git checkout -b one-branch
```

3. "hello,world"를 `README.md` 파일에 추가하고, 스테이징 영역 (staging area) 에 추가한 다음, "Added some changes to README.md"라는 메시지로 커밋 (commit) 합니다.

```shell
echo "hello,world" >> README.md
git add .
git commit -am "Added some changes to README.md"
```

4. `master` 브랜치로 전환합니다.

```shell
git checkout master
```

5. 로컬 `master` 브랜치가 원격 저장소와 최신 상태인지 확인합니다.

```shell
git pull
```

6. `one-branch`를 `master` 브랜치에 리베이스합니다.

```shell
git rebase one-branch
```

7. 리베이스 과정에서 발생하는 모든 충돌 (conflict) 을 해결합니다.

`git log`를 실행한 결과는 다음과 같습니다.

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
