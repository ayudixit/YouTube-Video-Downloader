from pytube import YouTube # Importing the YouTube class from pytube library
import tkinter as tk # Importing tkinter module for creating GUI
from tkinter import filedialog # Importing filedialog module from tkinter for creating file dialog

def download_video(url, save_path): # Defining the download_video function that takes url and save_path as arguments
    try: # Wrapping the function code in a try block to catch any exceptions


        yt = YouTube(url) 
        
#Working of this one line {line no. 7}:
# Creates a YouTube object for a specific video based on its url
# Takes the url string as input
# Returns the new YouTube object as output
# Uses the YouTube class as a blueprint for creating a tailored yt object for the given url
# Allows us to encapsulate the video-specific operations and data within this yt object
# By creating the yt object here, the later code can simply call methods on it to download 
# the video or get other info. 
# This encapsulates the video-specific work into this yt instance.
        


        streams = yt.streams.filter(progressive=True, file_extension="mp4")  

        

#The code at line 19 of youtube.py filters the available streams and gets the highest resolution MP4 video stream.

# The purpose of this code is to select the best quality downloadable video file from the available options. 
# It takes the yt.streams object as input, which contains all the possible video streams for the YouTube video.
# It first calls the filter() method on yt.streams to narrow down the options. 
# The filter keeps only progressive streams (as opposed to adaptive/DASH streams) and only streams with MP4 file extension.
# This filters out any streams that are not direct downloadable MP4 files. 
# It then calls get_highest_resolution() on the filtered streams object to select the single stream with the highest video resolution.
# The output is a PyTube Stream object containing the highest quality MP4 video file that can be downloaded.
# By filtering and selecting the highest resolution MP4, this code finds the best quality downloadable version of the video programmatically. 
        
# The key steps are:

# 1. Filter streams to progressive MP4 only
# 2. Get highest resolution from filtered streams
# 3. Return the highest res progressive MP4 stream
        
# This automates selecting the best file to download without the user having to inspect all available options and pick manually. 
# The core logic filters, sorts and returns the optimal stream for download.
        
        highest_res_stream = streams.get_highest_resolution() # Getting the highest resolution stream
        highest_res_stream.download(output_path=save_path) # Downloading the stream to the specified output path
        print("video downloaded successfully") # Displaying the success message
    except Exception as e: # Catching any exceptions
        print(e) # Displaying the error message

# Prompting the user for a YouTube URL and storing it in the 'url' variable
url = input("Enter a YouTube URL: ")

# Opening the file dialog and storing the selected directory in the 'save_path' variable
save_path = filedialog.askdirectory()

# Calling the download_video function with 'url' and 'save_path' as arguments
download_video(url, save_path)