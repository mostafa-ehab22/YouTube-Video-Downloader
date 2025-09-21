import yt_dlp
import sys
import os

"""
YouTube Video Downloader using yt-dlp - Mostafa Ehab 🐦‍🔥

Description:
    Downloads YouTube videos using yt-dlp library, which is more stable
    and actively maintained compared to pytube.
    
Usage:
    python yt_dlp_downloader.py "YOUTUBE_VIDEO_URL"
    
Example:
    python yt_dlp_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
Requirements:
    - yt-dlp library: pip install yt-dlp
"""

def get_video_info(url):
    """
    Extract video information without downloading.
    
    Args:
        url (str): YouTube video URL
        
    Returns:
        dict: Video information dictionary
    """
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info
        except Exception as e:
            raise Exception(f"Failed to extract video info: {e}")

def display_available_formats(info):
    """
    Display available video formats/resolutions.
    
    Args:
        info (dict): Video information dictionary
        
    Returns:
        list: Available format options
    """
    formats = []
    print("\nAvailable formats:")
    print("-" * 60)
    
    # Filter for video formats with both video and audio
    video_formats = [f for f in info['formats'] 
                    if f.get('vcodec') != 'none' and f.get('acodec') != 'none']
    
    # Get unique resolutions
    resolutions = {}
    for fmt in video_formats:
        height = fmt.get('height')
        if height:
            key = f"{height}p"
            if key not in resolutions:
                resolutions[key] = fmt
                filesize = fmt.get('filesize') or fmt.get('filesize_approx', 0)
                size_mb = filesize / (1024 * 1024) if filesize else 0
                
                formats.append({
                    'resolution': key,
                    'format_id': fmt['format_id'],
                    'size_mb': size_mb,
                    'ext': fmt.get('ext', 'unknown')
                })
    
    # Sort by resolution (highest first)
    formats.sort(key=lambda x: int(x['resolution'][:-1]), reverse=True)
    
    for i, fmt in enumerate(formats, 1):
        size_str = f"{fmt['size_mb']:.1f} MB" if fmt['size_mb'] > 0 else "Unknown size"
        print(f"{i}. {fmt['resolution']} ({fmt['ext']}) - {size_str}")
    
    return formats

def download_video(url, format_choice, output_path):
    """
    Download video with specified format.
    
    Args:
        url (str): YouTube video URL
        format_choice (str): Format selector
        output_path (str): Download directory path
    """
    ydl_opts = {
        'format': format_choice,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"\nDownloading video...")
            print("Please wait, this may take a while...")
            ydl.download([url])
            return True
        except Exception as e:
            print(f"Download failed: {e}")
            return False

def main():
    """
    Main function for YouTube video downloading.
    """
    # Validate command line arguments
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        sys.exit("Usage: python yt_dlp_downloader.py <YOUTUBE_VIDEO_URL>")
    
    video_url = sys.argv[1]
    print(f"Processing URL: {video_url}")
    
    # Get video information
    try:
        print("Fetching video information...")
        video_info = get_video_info(video_url)
    except Exception as e:
        sys.exit(f"Error: {e}")
    
    # Display video information
    print("\n" + "="*60)
    print("VIDEO INFORMATION")
    print("="*60)
    print(f"Title: {video_info.get('title', 'Unknown')}")
    print(f"Uploader: {video_info.get('uploader', 'Unknown')}")
    print(f"Duration: {video_info.get('duration', 0) // 60}:{video_info.get('duration', 0) % 60:02d}")
    print(f"View Count: {video_info.get('view_count', 0):,}")
    print("="*60)
    
    # Ask for confirmation
    confirmation = input("\nDo you want to download this video? (y/n): ").strip().lower()
    if confirmation != 'y':
        print("Download cancelled.")
        return
    
    # Display available formats
    try:
        formats = display_available_formats(video_info)
        if not formats:
            print("No suitable formats found.")
            return
    except Exception as e:
        print(f"Error getting formats: {e}")
        return
    
    # Get user's format choice
    while True:
        try:
            choice = input(f"\nChoose format (1-{len(formats)}) or 'best' for highest quality: ").strip().lower()
            
            if choice == 'best':
                format_selector = 'best[height<=1080]'  # Best quality up to 1080p
                break
            else:
                choice_num = int(choice)
                if 1 <= choice_num <= len(formats):
                    selected_format = formats[choice_num - 1]
                    format_selector = f"best[height<={selected_format['resolution'][:-1]}]"
                    break
                else:
                    print(f"Invalid choice. Please enter 1-{len(formats)} or 'best'")
        except ValueError:
            print("Invalid input. Please enter a number or 'best'")
    
    # Set up download directory
    download_path = "D:\\Mostafa\\YT Videos"
    
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)
            print(f"Created download directory: {download_path}")
    except Exception as e:
        print(f"Warning: Could not create directory {download_path}: {e}")
        download_path = "."
        print("Downloading to current directory instead.")
    
    # Download the video
    success = download_video(video_url, format_selector, download_path)
    
    if success:
        print(f"\n✓ Download completed successfully!")
        print(f"File saved to: {download_path}")
    else:
        print(f"\n✗ Download failed!")

if __name__ == "__main__":
    main()
