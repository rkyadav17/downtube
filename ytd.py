from pytube import YouTube
import os

# Enter the URL of the video
url = input("Enter the URL of the YouTube video: ")

# Create a YouTube object
yt = YouTube(url)

# Get the audio stream
audio = yt.streams.filter(only_audio=True).first()

# Set the output directory and file name
output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
output_file = input("Enter the output file name: ") + ".mp3"
output_path = os.path.join(output_dir, output_file)

# Download the audio stream
print("Downloading...")
audio.download(output_path=output_path, filename=output_file)

# Get the extension of the downloaded file
file_extension = os.path.splitext(output_file)[1]
print(f"Downloaded file extension: {file_extension}")
print("Download complete!")
