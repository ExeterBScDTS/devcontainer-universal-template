#!/bin/bash


hostdir=/home/mike/github/ExeterBScDTS/devcontainer-universal-template/ffmpeg/samples


#docker run --user 1000:1000 -v ${hostdir}:/tmp/workdir -w /tmp/workdir \
#        jrottenberg/ffmpeg \
#        -i test.ogg \
#        test-converted.mp3

docker run --user 1000:1000 -v ${hostdir}:/tmp/workdir -w /tmp/workdir \
        jrottenberg/ffmpeg \
        -i recording.ogg -i recording.webm \
        -f srt -i recording.srt \
        -acodec copy -vcodec copy  \
        -c:s srt \
        test-combined.mkv

# To generate mp4 will require transcoding
#docker run --user 1000:1000 -v ${hostdir}:/tmp/workdir -w /tmp/workdir \
#        jrottenberg/ffmpeg:snapshot-ubuntu \
#        -i test.ogg -i test.webm \
#        -acodec copy  -c:v libx264 -f mp4 \
#        test-combined.mp4