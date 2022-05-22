# Tips of making gif movies for websites

## Making mp4 videos from image series

- I use [Fiji](https://imagej.net/software/fiji/) for general image processing and static text annotation.
- Image stacks were exported to tif image sequences and made into H.264 encoded mp4 videos using "make-movie.py", which is a Python wrapper of [ffmpeg](https://www.ffmpeg.org/) that I previously wrote.

  ```
  usage: python make-movie.py [-h] folder fps target_size [n_digit_ImgID] [quality]

  positional arguments:
    folder         folder containing the image sequence for movie making
    fps            playback speed in frames per second
    target_size    the desired file size in MB
    n_digit_ImgID  optional; the digit number of image IDs of the image
                   sequence; default 4
    quality        optional; quality, 0 highest, 63 lowest; default 0

  optional arguments:
    -h, --help     show this help message and exit
  ```

  For example, the following command makes the image sequence stored in '\~/branching-paper/movie-1' into a '.mp4' movie at 12 fps and with a file size under 15 MB. The movie is saved in the parental folder of the image sequence folder ('\~/branching-paper/'):
  ```bash
  python make-movie.py ~/branching-paper/movie-1 12 15
  ```


## Use iMovie to make movies with title animations

- The title animations and editing features of Apple's iMovie can be useful for various purposes.
- Default title animations have black background. To use a different color, make an image with the desired color and apply the title on this background.
- Some title animations have a shadow effect that has no straightforward way to remove. Following [this post](https://discussions.apple.com/thread/5568794), a work-around is to copy text from Apple's Notes App to iMovie's title, and then format the text with desired font and color.


## Use ffmpeg to convert mp4 videos to high quality gifs

- I followed [this post](http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html) to make gifs with ffmpeg.
- See gifenc.sh for an example script to use customized palette in the gif with two passes.
