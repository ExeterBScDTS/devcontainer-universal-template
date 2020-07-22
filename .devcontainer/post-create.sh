#!/bin/bash
# Michael Saunby, July 2020. 
# https://github.com/msaunby

    # On my system /etc/group has a gid of 128 for the group docker, the ownership
	# of /var/run/docker.sock is root.docker, and my user account is a member of group docker.
	# By setting up a group within this container with the same gid the docker command can
	# run as the non priviliged user (codespace).  Anyway, the following works for me.
	# If it doesn't work for you I suggest either use "sudo docker" or set the group by hand.
	#
	# Note that for the group membership to be known to the shell it will be necessary to
	# restart, not rebuild, the container.
	DOCKER_GID=`stat --format="%g" /var/run/docker.sock` \
    && sudo groupadd -g ${DOCKER_GID} host-docker \
	&& sudo usermod -aG host-docker codespace

	
