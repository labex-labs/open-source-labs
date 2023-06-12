# Configure Docker Cloud to Automatically Build Docker Images

One of the most powerful features of Docker Cloud is the ability to define end-to-end CI/CD pipelines. In this part of the lab, you're going to link your GitHub account to Docker Cloud to facilitate seamless application delivery.

Let's start by linking your Docker Cloud account to your GitHub account:

1. Using your web browser, go to <a href="https://cloud.docker.com">https://cloud.docker.com</a> and sign in with your Docker ID.

2. Click the **Cloud Settings** link in the menu on the left hand side of the Docker Cloud web UI.

> **Note**: If you cannot see menu on the left, un-select **Swarm Mode** at the top of the screen.

3. Scroll down to the **Source providers** section. Click the **power plug** icon next to GitHub, and follow the procedure to link your GitHub account.

Now that you've got Docker Cloud linked to your GitHub account, we'll start by forking a demo repo.

1. In your web browser, navigate to <a href="https://github.com/Cloud-Demo-Team/voting-demo.git"> https://github.com/Cloud-Demo-Team/voting-demo.git</a>.

2. Click the **Fork** button in the upper right hand corner to create your own copy of the source repository.

Next, we'll clone the repository into our local Docker environment. The following commands will be executed in the terminal or command window from Linux **node0**

1.  At the command line, change into the directory where you want to clone code.

2.  Clone the repository (you will need to have `git` installed and the `git` binary present in your PATH).

        $ git clone https://github.com/<your github user name>/voting-demo.git

        Cloning into 'voting-demo'...
        remote: Counting objects: 481, done.
        remote: Total 481 (delta 0), reused 0 (delta 0), pack-reused 481
        Receiving objects: 100% (481/481), 105.01 KiB | 0 bytes/s, done.
        Resolving deltas: 100% (246/246), done.
        Checking connectivity... done.

This will create a copy of the forked repo in a directory called `voting-demo` within your home directory.
