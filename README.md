# Media files extractor

If you have a folder with media files, but you don't want to extract from
    there manually, this script will help you extract all media data
    automatically. It searches for all the formats you need recursively,
    creates a folder for each format separately, and copies them there.


## Installation

1) ```
   git clone https://github.com/zhandos256/mediafilesextractor.git
   ```
2) ```
   pip install -r requirements.txt
   ``` 
3) ```
   run main.py
   ```

## File Formats

Script have next formats

* Audio (mp3, opus, flac, aac, wav, wma)
* Video (mp4, webm, flv, vob, ogv, ogg, avi, wmv, m4p, m4v, 3gp)
* Images (jpg, jpeg, png, webp, gif, svg, avif, apng)

> Note `if scipt don't find your formats, just add you formats to formats.py`