# Using ffmpeg docker image to convert media file formats


## Video file formats

Files commonly described as video formats are also known as *containers*, because
they contain more than one *stream* of data, typically a video stream and an audio stream. The use of
the term *container* in this context might be rather confusing, so in most cases I'll refer to them as
files.

There are several video file formats (containers) such MP4. <https://en.wikipedia.org/wiki/MPEG-4_Part_14>  Note that MP4 supports different encodings of video and audio streams, and
each of these encodings has countless variations, for example the sample rate, the resoultion, stereo or mono.

### Browser compatibility

The most widely used web browsers have multimedia capabilities, and can play video and audio streams from the web and local files. Web browsers often have the capability to create live multimedia sources by accessing camera and microphone, and in many cases can now also screen share and audio playback.


[MDN: Web media technologies](https://developer.mozilla.org/en-US/docs/Web/Media)




<https://docs.docker.com/engine/security/userns-remap/>

```sh
# To find mounted volumes.
# Assume this development container is the only running container.
# This should be true when running in Azure Codespaces.
sudo docker inspect -f "{{ .Mounts }}" `sudo docker ps -q`

sudo docker run --user 1000 -v $(pwd):$(pwd) -w $(pwd) -it --entrypoint='bash' jrottenberg/ffmpeg
```

## Ffmpeg

<https://ffmpeg.org/>

Ffmpeg is a cross-platform open source tool for converting between streaming media formats.  It's very powerful with lots of options and support for very many formats, but this means it has a lot of library dependencies and isn't always easy to install.

For our purposes a Docker image makes using ffmpeg much easier.

## Docker image

See <https://hub.docker.com/r/jrottenberg/ffmpeg/>

```sh
docker run -v $(pwd):$(pwd) -w $(pwd)\
        jrottenberg/ffmpeg -stats \
        -i original.gif \
        original-converted.mp4
```

###  Merge audio and video tracks

```sh
ffmpeg -i audio.aiff -i video.mov -acodec copy -vcodec copy -f mp4 avcombined.mp4
```
