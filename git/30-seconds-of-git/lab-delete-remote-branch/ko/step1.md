# 원격 브랜치 삭제

때로는 더 이상 필요하지 않은 원격 브랜치를 삭제해야 할 수 있습니다. 예를 들어, 기능 브랜치가 메인 브랜치에 병합된 경우, 저장소를 깨끗하게 유지하기 위해 원격 기능 브랜치를 삭제할 수 있습니다.

`git-playground`라는 GitHub 저장소가 GitHub 계정에서 복제되었고, 이는 `https://github.com/labex-labs/git-playground.git`의 포크에서 파생되었다고 가정해 보겠습니다. 더 이상 필요하지 않은 `feature-branch`라는 원격 브랜치를 삭제하려고 합니다. 원격 브랜치를 삭제하는 단계는 다음과 같습니다.

1. 저장소를 복제하고, 디렉토리로 이동하여 ID 를 구성합니다.
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. `feature-branch` 브랜치를 `origin` 원격 저장소에 추가합니다.
   ```shell
   git checkout -b feature-branch
   git push -u origin feature-branch
   ```
3. `git branch -r` 명령을 사용하여 모든 원격 브랜치를 나열합니다.
   ```shell
   git branch -r
   ```
   출력에는 `feature-branch` 원격 브랜치가 포함되어야 합니다.
   ```
   origin/HEAD -> origin/master
   origin/feature-branch
   origin/master
   ```
4. `git push -d <remote> <branch>` 명령을 사용하여 지정된 `<remote>`에서 지정된 원격 `<branch>`를 삭제합니다.
   ```shell
   git push -d origin feature-branch
   ```
   이 명령은 `origin` 원격 저장소에서 `feature-branch` 원격 브랜치를 삭제합니다.
5. `git branch -r` 명령을 다시 사용하여 원격 브랜치가 삭제되었는지 확인합니다.
   ```shell
   git branch -r
   ```
   출력에는 `feature-branch` 원격 브랜치가 포함되지 않아야 합니다.
   ```
   origin/HEAD -> origin/master
   origin/master
   ```
