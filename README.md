# TikTok Video Scheduler

An automated TikTok video scheduling tool that transcribes video content, generates AI-powered descriptions and hashtags, and schedules uploads to TikTok.

## Features

- **Automated Video Processing**: Batch process videos from a specified folder.
- **AI-Powered Content Generation**: Uses OpenAI Whisper for transcription and Ollama/LLaMA for content generation.
- **Smart Scheduling**: Automatically schedules videos in TikTok.
- **Content-Aware Descriptions**: Generates catchy, 15-word maximum descriptions based on video content.
- **Intelligent Hashtag Generation**: Creates 5 content-specific hashtags plus fallback trending tags.
- **Chrome Integration**: Uses Selenium with Chrome for reliable uploads.
- **Error Handling**: Comprehensive error handling with fallback options.

## Prerequisites

### Required Software
- Python 3.7+
- Chrome browser
- ChromeDriver
- Ollama with LLaMA 3.1 model
- FFmpeg (for audio processing)

### Python Dependencies
All required packages are listed in `requirements.txt`. Install them using:
```bash
pip install -r requirements.txt
```

Key dependencies include:
- `selenium` - Web automation
- `tiktok-uploader` - TikTok upload functionality
- `openai-whisper` - Audio transcription
- `subprocess` - System process management

### Ollama Setup
1. Install Ollama from [https://ollama.ai](https://ollama.ai)
2. Pull the LLaMA 3.1 model:
   ```bash
   ollama pull llama3.1
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/soualahmohammedzakaria/TikTok-Automation
   cd TikTok-Automation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your configuration:
   - Create a `config.py` file with your `VIDEO_FOLDER` path
   - Place your TikTok cookies in `cookies.txt`

## Configuration

### config.py
```python
VIDEO_FOLDER = "/path/to/your/videos"
```

### cookies.txt
Export your TikTok cookies and save them in the root directory as `cookies.txt`. This is required for authentication.

## Usage

### Basic Usage
```bash
python tiktok_video_uploader.py
```

### File Structure
```
project/
├── .gitignore             # Git ignore file
├── tiktok_video_uploader.py  # Main scheduler script
├── video_analyzer.py       # Video analysis and content generation
├── config.py              # Configuration settings
├── cookies.txt            # TikTok authentication cookies
├── requirements.txt       # Python dependencies
└── videos/                # Your video files directory
```

## How It Works

1. **Video Discovery**: Scans the `VIDEO_FOLDER` for video files
2. **Content Analysis**: 
   - Transcribes audio using OpenAI Whisper (tiny model)
   - Generates description using Ollama/LLaMA 3.1
   - Creates relevant hashtags based on content
3. **Scheduling**: Uploads videos every 2 days starting tomorrow at 2 PM
4. **Upload**: Uses tiktok-uploader with Chrome automation

## Chrome Options
The tool uses optimized Chrome settings for headless operation:
- `--no-sandbox`: Bypasses OS security model
- `--disable-dev-shm-usage`: Overcomes limited resource problems
- `--disable-gpu`: Disables GPU hardware acceleration
- `--disable-features=VizDisplayCompositor`: Disables compositor

## Output Format

For each video, the tool generates:
```
✅ Scheduled: /path/to/video.mp4 at 2025-07-17 14:00:00
Description: AI-generated catchy description #hashtag1 #hashtag2 #hashtag3 #hashtag4 #hashtag5 #fyp #viral #trending #foryou #tiktok
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the project's coding standards and includes appropriate tests.

## License

This project is for educational purposes. Ensure compliance with TikTok's Terms of Service and API guidelines.

## Disclaimer

This tool is for educational use only. Users are responsible for complying with TikTok's Terms of Service and community guidelines. The authors are not responsible for any misuse of this tool.
