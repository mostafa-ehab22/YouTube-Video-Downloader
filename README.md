# 🎬 YouTube Video Downloader

A simple, reliable YouTube video downloader built with Python using `yt-dlp`. Download your favorite videos in various quality options with an easy-to-use command-line interface.

## 🚀 Features

- ⚡ **Fast & Reliable**: Built with `yt-dlp` for maximum compatibility
- 🎯 **Quality Selection**: Choose from available resolutions (360p, 720p, 1080p, etc.)
- 📊 **Video Information**: Display title, uploader, duration, and view count before downloading
- 📁 **Custom Output**: Automatically organizes downloads in a designated folder
- 🛡️ **Error Handling**: Robust error handling with helpful error messages
- 🔄 **Format Detection**: Automatically detects and displays available video formats
- 💾 **Size Preview**: Shows estimated file sizes for each quality option

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Install Dependencies

```bash
pip install yt-dlp
```

### Download the Script

```bash
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
```

## 🚀 Usage

### Basic Usage

```bash
python ytdownloader.py "YOUTUBE_VIDEO_URL"
```

### Examples

```bash
# Download a single video
python ytdownloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download with shortened URL
python ytdownloader.py "https://youtu.be/dQw4w9WgXcQ"
```

### Interactive Process

1. **🔍 Video Information**: The script will fetch and display video details
2. **✅ Confirmation**: Confirm if you want to download the video
3. **📋 Format Selection**: Choose from available quality options
4. **⬇️ Download**: The video downloads to your specified directory

### Sample Output

```
Processing URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Fetching video information...

============================================================
VIDEO INFORMATION
============================================================
Title: Rick Astley - Never Gonna Give You Up (Official Video)
Uploader: Rick Astley
Duration: 3:33
View Count: 1,234,567,890
============================================================

Do you want to download this video? (y/n): y

Available formats:
------------------------------------------------------------
1. 1080p (mp4) - 85.2 MB
2. 720p (mp4) - 45.8 MB
3. 480p (mp4) - 25.3 MB
4. 360p (mp4) - 15.1 MB

Choose format (1-4) or 'best' for highest quality: 2

Downloading video...
Please wait, this may take a while...

✓ Download completed successfully!
File saved to: D:\Mostafa\YT Videos
```

## ⚙️ Configuration

### Custom Download Directory

By default, videos are saved to `D:\Mostafa\YT Videos`. To change this, modify the `download_path` variable in the script:

```python
download_path = "YOUR/CUSTOM/PATH"
```

### Quality Options

- **Numbers (1, 2, 3, etc.)**: Select specific quality from the list
- **"best"**: Automatically choose the highest quality (up to 1080p)

📂 Project Structure
```
📂 youtube-downloader/
├── ytdownloader.py          ⬅️ Main script
├── README.md                ⬅️ This file
└── LICENSE                  ⬅️ MIT License
```

## 🔧 Troubleshooting

### Common Issues

**❌ "Failed to extract video info"**
- Check if the URL is valid and accessible
- Ensure the video is not private or region-blocked
- Update yt-dlp: `pip install --upgrade yt-dlp`

**❌ "No suitable formats found"**
- The video might be a live stream or have restricted formats
- Try a different video URL

**❌ Permission errors**
- Ensure you have write permissions to the download directory
- Try running as administrator (Windows) or with sudo (Linux/Mac)

### Updating yt-dlp

Keep yt-dlp updated for the best compatibility:

```bash
pip install --upgrade yt-dlp
```

## 🆚 Why yt-dlp over pytube?

| Feature | yt-dlp | pytube |
|---------|---------|---------|
| 🔄 Updates | Regular | Infrequent |
| 🛡️ Stability | High | Low |
| 🌐 Site Support | 1000+ sites | YouTube only |
| 🐛 Bug Fixes | Fast | Slow |
| 📱 Maintenance | Active | Limited |

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

- This tool is for educational purposes and personal use only
- Respect YouTube's Terms of Service and copyright laws
- Only download videos you have permission to download
- Consider supporting content creators through official channels

## 🙏 Acknowledgments

- Thanks to the [yt-dlp](https://github.com/yt-dlp/yt-dlp) developers for creating an amazing tool
- Inspired by the need for a reliable YouTube downloader
