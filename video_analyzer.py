import whisper
import re
import subprocess
import warnings

# Suppress warnings from Whisper about FP16 on CPU
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Initialize Whisper model
whisper_model = whisper.load_model("tiny")

# Transcribe audio from video
def transcribe_audio(video_path):
    print("🔊 Transcribing audio...")
    result = whisper_model.transcribe(video_path)
    return result["text"]

# Generate a catchy description
def generate_description(content):
    print("🪄 Generating description...")
    prompt = f'You are a social media expert. Create a 15-words-max catchy TikTok video description. You should respond with the description only without quotes. Here is the content: {content}'
    
    # Call Ollama via command line
    try:
        process = subprocess.Popen(
            ['ollama', 'run', 'llama3.1'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=prompt)
        
        if not stdout:
            print(f"⚠️ Error generating description: {stderr}")
            return "Important video to watch!"  # Fallback description
        
        # Clean up the response
        description = stdout.strip()
        description = re.sub(r'^"|"$', '', description)  # Remove surrounding quotes if any
        return description
        
    except Exception as e:
        print(f"⚠️ Error calling Ollama: {e}")
        return "Important video to watch!" # Fallback description

# Extract hashtags from content
def extract_tags(content):
    print("🏷️ Extracting tags...")
    prompt = f'You are a social media expert. Create 5 content-specific TikTok video hashtags separated with spaces for this content: {content}'
    fallback_tags = ["#fyp", "#viral", "#trending", "#foryou", "#tiktok"]
    
    # Call Ollama via command line
    try:
        process = subprocess.Popen(
            ['ollama', 'run', 'llama3.1'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=prompt)
        
        if not stdout:
            print(f"⚠️ Error generating hashtags: {stderr}")
            return fallback_tags  # Return fallback if no output
            
        # Split the response by spaces and keep only valid hashtags
        generated_tags = [tag for tag in stdout.strip().split() if tag.startswith("#")]
        
        # Always include fallback tags, removing duplicates
        combined_tags = list(dict.fromkeys(generated_tags + fallback_tags))
        
        return combined_tags
        
    except Exception as e:
        print(f"⚠️ Error calling Ollama: {e}")
        return fallback_tags  # Return fallback on error

# Generate description and tags for a video
def generate_description_and_tags(video_path):
    transcript = transcribe_audio(video_path)
    description = generate_description(transcript)
    tags = extract_tags(transcript)
    return description, tags