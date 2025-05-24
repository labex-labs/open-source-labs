# 원격 브랜치 이름 변경

이 랩을 완료하려면 GitHub 계정의 `git-playground` Git 저장소를 사용합니다. 이 저장소는 `https://github.com/labex-labs/git-playground.git`의 포크에서 가져온 것입니다. 포크할 때 "Copy master branch only"를 선택 해제하십시오.

`https://github.com/your-username/git-playground`라는 Git 저장소가 있습니다. `feature-branch`라는 브랜치를 생성하여 원격 저장소에 푸시했습니다. 이제 로컬과 원격 모두에서 브랜치 이름을 `new-feature-1`로 변경하려고 합니다.

1. 저장소를 복제하고, 디렉토리로 이동하여 ID 를 구성합니다.
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. `feature-branch` 브랜치로 전환합니다.
   ```shell
   git checkout feature-branch
   ```
3. 로컬과 원격 모두에서 브랜치 이름을 변경합니다.
   ```shell
   git branch -m feature-branch new-feature-1
   git push origin --delete feature-branch
   git push -u origin new-feature-1
   ```
4. 브랜치 이름이 변경되었는지 확인합니다.
   ```shell
   git branch -a
   ```

다음은 `git branch -a`를 실행한 결과입니다.

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```
