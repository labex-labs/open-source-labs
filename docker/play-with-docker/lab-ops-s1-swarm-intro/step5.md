# Scaling An Application

Let us pretend that our cats vs. dogs vote has gone viral and our two front-end web servers are no longer able to handle the load. How can we tell our app to add more replicas of our _vote_ service? In production you might automate it through Docker's APIs but for now we will do it manually. You could also edit the `docker-stack.yml` file and change the specs if you wanted to make the scale size more permanent. Type the following at the [node1] terminal:

```bash
docker service scale voting_stack_vote=5
```

Now enter your `docker stack services voting_stack` command again. You should see the number of replicas for the vote service increase to 5 and in a few seconds Swarm will have all of them running. Go back to your [front-end voting UI](/){:data-term=".term1"}{:data-port="5000"} and refresh the page a few times. You should see the _container ID_ listed at the bottom cycle through all 5 of your containers. If you go back and refresh your [SWARM VISUALIZER](/){:data-term=".term1"}{:data-port="8080"} you should see your updated architecture there as well.

Here's our new architecture after scaling:
![Swarm scaling](/images/ops-swarm-scale.svg)

That's all there is to it! Docker Swarm can easily and quickly scale your application's services up and down as needs require. Again, in many situations you would probably want to automate this rather than manually scaling, which is pretty easy through the Docker APIs. You also have the option to swap out the built-in load balancer for something with additional controls, like an [F5](https://store.docker.com/images/f5networks-asp) or [Citrix NetScaler](https://store.docker.com/images/netscaler-cpx-express) or some other software you prefer.
