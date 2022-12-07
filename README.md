# P3
# Exercise 1

For obtaining the HLS transport stream containers, we follow the following steps:
  1 - We read the video from the disk
  2 - We scale the video to multiple resolutions required
  3 - transcode each of the scaled videos to the required bitrates
  4 - transcode the audio to the required bitrates
  5 - combine the video and audio, package each combination, and create the individual TS segments and the playlists.
  6 - Create a master playlist that points to each of the variants
  
https://ottverse.com/hls-packaging-using-ffmpeg-live-vod/

# Exercise 4
The answer is in the file exercise4.pdf. Also, the file .ts used is segment_tv3.ts.
