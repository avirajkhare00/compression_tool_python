import os

#give a directory root
# give a file extension we want to catch
# store all those files inside an array

def input_dir(dir_name):

    for root, dirs, files in os.walk(dir_name, topdown=False):
        for name in files:
            #print(os.path.join(root, name))
            if os.path.splitext(os.path.join(root, name))[-1] == '.mp4':
                print os.path.join(root, name)
                #send all above filenames for ffmpeg conversion
                filter_video_files(os.path.join(root, name))
        #since we are not printing dirs
        #for name in dirs:
        #    print(os.path.join(root, name))

def filter_video_files(video_file_path):
    
    print video_file_path
    #we will call os.system() for ffmpeg compression
    #and will save it in same folder

#run the function

input_dir('/Users/avirajkhare00/Music')