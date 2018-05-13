import os

def input_dir(dir_name):

    for root, dirs, files in os.walk(dir_name, topdown=False):
        for name in files:
            if os.path.splitext(os.path.join(root, name))[-1] == '.mp4':
                if name.split('_')[-1] == "compressed.mp4":
                    pass
                else:
                    filter_video_files(os.path.join(root, name))

def filter_video_files(video_file_path):
    
    print video_file_path
    
    command = "ffmpeg -i " +  video_file_path + " -f mp4 -vcodec libx264 -preset medium -profile:v main -acodec aac " + video_file_path.split('.')[-2] + "_compressed.mp4"  + " -hide_banner"
    
    os.system(command)

    os.remove(video_file_path)

#run the function

input_dir('./')