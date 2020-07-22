#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

# To fully customize the contents of this image, use the following Dockerfile instead:
# https://github.com/microsoft/vscode-dev-containers/tree/v0.128.0/containers/codespaces-linux/.devcontainer/Dockerfile
FROM mcr.microsoft.com/vscode/devcontainers/universal:0-linux

# Install additional packages.
#
# Here we install moby (docker). Also taking the opportunity to remove the
# user from the docker group as there will be a different group called host-docker.
# See post-create.sh for more details.
RUN sudo apt-get update \
     && export DEBIAN_FRONTEND=noninteractive \
     && sudo deluser codespace docker \
     && sudo apt-get -y install --no-install-recommends moby-cli