from selenium.webdriver.chrome.options import Options
from tiktok_uploader.upload import upload_video
from config import VIDEO_FOLDER
from video_analyzer import generate_description_and_tags
import os
import datetime

# Create Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-features=VizDisplayCompositor')

# Get all videos from VIDEO_FOLDER
video_files = sorted([
    os.path.join(VIDEO_FOLDER, file)
    for file in os.listdir(VIDEO_FOLDER)
])

# Start scheduling from tomorrow at 2 PM local time
start_time = datetime.datetime.now().replace(hour=14, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)

for i, video_path in enumerate(video_files):
    schedule_time = start_time + datetime.timedelta(days=i * 2)  # Schedule every two days

    # Generate description and tags using the video analyzer
    description, tags = generate_description_and_tags(video_path)

    # Format the description and tags
    full_description = f"{description} {' '.join(tags)}"

    # Schedule the video upload
    try:
        upload_video(
            filename=video_path,
            description=full_description,
            cookies='cookies.txt',
            schedule=schedule_time,
            options=chrome_options # Pass Chrome options to the upload function
        )
        print(f"✅ Scheduled: {video_path} at {schedule_time}.\nDescription: {full_description}")
    except Exception as e:
        print(f"❌ Failed to upload {video_path} — {str(e)}")