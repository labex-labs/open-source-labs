# 로컬 Master 브랜치를 원격 브랜치와 일치하도록 재설정

프로젝트 작업을 진행하면서 로컬 `master` 브랜치에 변경 사항을 적용했습니다. 하지만 원격 `master` 브랜치가 로컬 브랜치에 없는 새로운 변경 사항으로 업데이트되었다는 것을 알게 되었습니다. 로컬 `master` 브랜치를 원격 브랜치와 일치하도록 재설정해야 합니다.

1. `master` 브랜치로 전환합니다:
   ```shell
   git checkout master
   ```
2. 원격 저장소에서 최신 업데이트를 가져옵니다:
   ```shell
   git fetch origin
   ```
3. 현재 브랜치의 커밋 기록을 확인합니다:
   ```shell
   git log
   ```
4. 로컬 `master` 브랜치를 원격 브랜치와 일치하도록 재설정합니다:
   ```shell
   git reset --hard origin/master
   ```
5. 로컬 `master` 브랜치가 이제 원격 `master` 브랜치와 최신 상태인지 확인합니다:
   ```shell
   git log
   ```

다음은 최종 결과입니다:

```shell
[object Object]
```
