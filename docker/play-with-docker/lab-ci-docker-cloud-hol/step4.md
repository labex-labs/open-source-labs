# Trigger an Autobuild

Switch back the command line of your VM.

1.  If you have not already log into your Azure VM. For example (be sure to use the actual node name supplied in your email):

    `ssh ubuntu@node0-gvs0mgc0216.southcentralus.cloudapp.azure.com`

1.  Change to the directory containing the voting app.

        $ cd ~/voting-demo/voting

1.  Use vi or your favorite text editor to open `app.py`.

- To use `vi` on Linux: `$ vi app.py`

1.  Scroll down to find the lines containing `optionA` and `optionB`, and change **Dev** and **Ops** to **Futbol** and **Soccer**.

        optionA = "Futbol"
        optionB = "Soccer"

1.  Save your changes.

1.  Commit changes to the repository and push to GitHub using `git add`, `git commit`, and `git push`.

        $ git add *
        $ git commit -m "changing the voting options"
        [master 2ab640a] changing the voting options
        1 file changed, 3 insertions(+), 2 deletions(-)
        $ git push origin master
        Counting objects: 4, done.
        Delta compression using up to 8 threads.
        Compressing objects: 100% (4/4), done.
        Writing objects: 100% (4/4), 380 bytes | 0 bytes/s, done.
        Total 4 (delta 3), reused 0 (delta 0)
        To https://github.com/<your github repo>/voting-demo.git
        c1788a1..2ab640a  master -> master

> **Note:** You may be prompted to set your email and name when you attempt to commit your changes. If this is the case, simply follow the instructions provided on your screen.
>
> **Note:** If you have two factor authentication (2FA) configured on your GitHub account you will need to enter your personal access token (PAT) instead of your password when prompted.

6. In the Docker Cloud web UI, navigate back to the **voting** repo and notice that the status is **BUILDING**.

   > **Note**: It can take several minutes for a build job to complete.

7. Click the **Timeline** tab near the top of the screen.

8. Click `Build in master:/voting`.

   Here you can see the status of the build process:

Congratulations! You have successfully configured Docker Cloud to automatically build a new Docker image each time you push a change to your application's repository on GitHub.

# Learn More

To learn more about Docker Cloud’s continuous integration (CI) capabilities and how to bring more automation and collaboration to your application pipeline, check out:

- **Video [Automated Builds with Docker Cloud](https://www.youtube.com/watch?v=sl2mfyjnkXk)**
- **Docs**: [Automated Builds](https://docs.docker.com/docker-cloud/builds/automated-build/)
