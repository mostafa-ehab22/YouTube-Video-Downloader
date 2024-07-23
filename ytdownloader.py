from pytube import YouTube
import sys
"""
Running program: python YTDownloader.py "LINK"
"""

def main():
    
    if len(sys.argv) != 2:
        sys.exit("Usage: python YTDownloader.py <LINK>")
    
    # Fetch video Link
    link = sys.argv[1]
    try:
        yt = YouTube(link)
    except Exception as e:
        sys.exit(f"Failed to fetch video: {e}")

    print(f"Title: {yt.title}")
    print(f"Views: {yt.views:,}")

    confirmation = input("Do you want to download video? (y/n): ").strip().lower()

    if confirmation == 'y':
        # Getting Video Resolution
        resolution_input = input("Choose resolution (e.g., 720): ").strip()
        resolution = yt.streams.filter(res=f"{resolution_input}p",progressive=True).first()

        try:
            # Checking if wanted resolution available
            if resolution:
                resolution.download("D:\Mostafa\YT Videos")
                print("Download Successful!")
            else:
                print("Video Resolution not available")

        except Exception as e:
            print(f"Couldn't download video: {e}")


if __name__ == "__main__":
    main()