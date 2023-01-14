import subprocess

def m3u_to_m3u8(filepath):
    # use ffmpeg to convert m3u to m3u8
    subprocess.run(["ffmpeg", "-i", filepath, "-c", "copy", "-bsf:a", "aac_adtstoasc", "-hls_time", "10", "-hls_list_size", "0", "-f", "hls", filepath.replace('.m3u','.m3u8')])

# Usage
m3u_to_m3u8('path/to/file.m3u')
