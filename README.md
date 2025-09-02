# Kubernetes - Hello World

Project for learning purposes.

## Abstract

Started with a minimal kubernetes configuration in `k8s` and `hello-world.py`,
I add more and more of functionality and quality assurance tools.

## My Computational Setup

I have a Raspberry Pi 5 named `cluster`, with kubernetes distribution `k3s`
running on it. It is not really a cluster, and does not feature the main
selling points of kubernetes: redundancies and fault tolerance.
However for learning the basics, a single machine on my desk is perfect.

CI tools (Gitea, Gitea Runner) run on another Raspberry Pi 5. Code is mirrored
to GitHub, but not executed there.

## Installing

The majority of this project is to figure out how to set it up. Depending on your
setup you might need to figure out how to ...
* [Upgrade Debian](https://linuxconfig.org/how-to-upgrade-debian-to-latest-version)
* [Install kubernetes](https://docs.k3s.io/installation)
* [Using Secrets with Gitea](https://docs.gitea.com/usage/actions/secrets)
  to push configurations
* [Using Secrets with kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/)
  to pull images

Asking an AI assistant of your choice might help,.. or screw things up.
