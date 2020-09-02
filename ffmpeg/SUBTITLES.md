https://www.videoindexer.ai

https://stackoverflow.com/questions/8672809/use-ffmpeg-to-add-text-subtitles

```sh
ffmpeg -i input.mp4 -f srt -i input.srt \
-map 0:0 -map 0:1 -map 1:0 -c:v copy -c:a copy \
-c:s mov_text output.mp4


ffmpeg -i input.mp4 -f srt -i input.srt \
-map 0:0 -map 0:1 -map 1:0 -c:v copy -c:a copy \
-c:s srt  output.mkv
```