FROM jenkins/jenkins:alpine
# consider switching to lts image
# FROM jenkins/jenkins:lts

# Plugins for better UX (not mandatory)
RUN /usr/local/bin/install-plugins.sh ansicolor
RUN /usr/local/bin/install-plugins.sh greenballs

# Plugin for scaling Jenkins agents
RUN /usr/local/bin/install-plugins.sh kubernetes
# su to root to install some things
USER root
# install docker
RUN apk update && apk add docker && apk add openrc && rc-update add docker boot
# su to jenkins user
USER jenkins