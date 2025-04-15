# Solutions

```shell
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
