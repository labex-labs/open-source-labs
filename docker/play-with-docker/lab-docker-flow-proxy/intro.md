# Introduction

In this lab, we will leverage the power of Docker Swarm Mode, released with Docker 1.13, and the great features of vfarcic **[Docker Flow Proxy](http://proxy.dockerflow.com/swarm-mode-stack/)** which provide an easy way to reconfigure proxy every time a new service is deployed, or when a service is scaled. It uses docker **service labels** to define the metadata and rules for its dynamically-configured routing rules to send traffic from the PRoxy to real applications (regardless of the host they are within a Docker Swarm Cluster).
