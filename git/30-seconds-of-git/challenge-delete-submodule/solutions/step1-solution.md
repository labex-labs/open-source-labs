```shell
git submodule deinit -f -- <submodule>
rm -rf .git/modules/<submodule>
git rm -f <submodule>

git submodule deinit -f -- 30code
rm -rf .git/modules/30code
git rm -f 30code
# Removes the `30code` submodule
```

```shell
cd git
git submodule status
git submodule deinit -f -- sha1collisiondetection
rm -rf .git/modules/sha1collisiondetection
git rm -f sha1collisiondetection
git submodule status
```
