# ffmpeg_compress

This tool is used to compress any video file to .H264 format.
Just provide folder path, script will walk down in directory tree and catches for mp4, avi files. Other file types and options will be included later.

### Features
 - Conversion to .H264 format to compress video.
 - Delete old video after compresion.

### TODO
 - Create module structure and architecture for this repo.
 - Update documentation completely.
 - Make a simple Desktop App to sync file structure and show all video files using [electronjs](https://electronjs.org/).
 - Add Google Drive API to offload file to cloud after compression.
 - Create Android/iOS app with same functionality.
 - Create a new pull request to add more.

### Installation
 ```sh
    $ git clone https://github.com/avirajkhare00/compression_tool_python
    $ cd compression_tool_python
    $ mkdir .env
    $ cd .env
    $ virtualenv compression_tool_python
    $ source compression_tool_python/bin/activate
 ```
 After creating vitrual enviroment for python, install ffmpeg depending on OS you are using.
 Finally run-
```sh
    (compression_tool_python) $ python app.py
```

