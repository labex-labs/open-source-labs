# Testing Docker capabilities

In this step you will start various new containers. Each time you will use the commands learned in the previous step to tweak the capabilities associated with the account used to run the container.

1. Start a new container and prove that the container's root account can change the ownership of files.

   ```bash
   docker run --rm -it alpine chown nobody /
   ```

   The command gives no return code indicating that the operation succeeded. The command works because the default behavior is for new containers to be started with a root user. This root user has the CAP_CHOWN capability by default.

2. Start another new container and drop all capabilities for the containers root account other than the CAP_CHOWN capability. Remember that Docker does not use the "CAP\_" prefix when addressing capability constants.

   ```bash
   docker run --rm -it --cap-drop ALL --cap-add CHOWN alpine chown nobody /
   ```

   This command also gives no return code, indicating a successful run. The operation succeeds because although you dropped all capabilities for the container's `root` account, you added the `chown` capability back. The `chown` capability is all that is needed to change the ownership of a file.

3. Start another new container and drop only the `CHOWN` capability form its root account.

   ```bash
   docker run --rm -it --cap-drop CHOWN alpine chown nobody /
   ```

   ```
    chown: /: Operation not permitted
   ```

   This time the command returns an error code indicating it failed. This is because the container's root account does not have the `CHOWN` capability and therefore cannot change the ownership of a file or directory.

4. Create another new container and try adding the `CHOWN` capability to the non-root user called `nobody`. As part of the same command try and change the ownership of a file or folder.

   ```bash
   docker run --rm -it --cap-add chown -u nobody alpine chown nobody /
   ```

```

chown: /: Operation not permitted

```

The above command fails because Docker does not yet support adding capabilities to non-root users.

In this step you have added and removed capabilities to a range of new containers. You have seen that capabilities can be added and removed from the root user of a container at a very granular level. You also learned that Docker does not currently support adding capabilities to non-root users.
