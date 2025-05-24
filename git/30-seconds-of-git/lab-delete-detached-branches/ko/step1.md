# 분리된 브랜치 삭제

더 이상 필요하지 않은 여러 개의 분리된 브랜치가 있는 Git 저장소가 있습니다. 이러한 브랜치들은 저장소를 복잡하게 만들고 관리를 어렵게 합니다. 저장소를 정리하기 위해 모든 분리된 브랜치를 삭제하려고 합니다.

이 랩을 완료하려면 GitHub 계정의 `git-playground` Git 저장소를 사용합니다. 이 저장소는 `https://github.com/labex-labs/git-playground.git`의 포크에서 가져온 것입니다. "master 브랜치만 복사"를 선택하지 마십시오.

1. 저장소를 복제하고, 디렉토리로 이동하여 ID 를 구성합니다.

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. 원격 저장소에 `feature-branch` 브랜치가 있으므로, `feature-branch`로 전환합니다. 이렇게 하면 로컬 `feature-branch`가 원격 저장소의 `feature-branch` 브랜치를 추적하게 되고, 원격 저장소의 `feature-branch` 브랜치가 삭제됩니다.

```shell
git checkout feature-branch
git push origin --delete feature-branch
```

3. 로컬 브랜치와 추적하는 원격 브랜치 간의 추적 관계를 확인합니다.

```shell
git branch -vv
```

4. `master` 브랜치로 다시 전환합니다.

```shell
git checkout master
```

5. 로컬 저장소에서 모든 분리된 브랜치를 제거합니다.

```shell
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

6. 분리된 브랜치가 삭제되었는지 확인합니다.

```shell
git branch
```

출력에는 특정 브랜치와 연결된 브랜치만 표시되어야 합니다.

```shell
* master d22f46b [origin/master] Added file2.txt
```
