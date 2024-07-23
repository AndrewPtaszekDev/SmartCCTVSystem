import os
import requests

# URL for the YOLO model files
weights_url = 'https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights'
cfg_url =  'https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg'

home_dir = os.path.expanduser("~")
target_dir = os.path.join(home_dir, '.cvlib', 'object_detection', 'yolo', 'yolov3')

os.makedirs(target_dir, exist_ok=True)

# Path for the files
weights_path = os.path.join(target_dir, 'yolov4-tiny.weights')
cfg_path = os.path.join(target_dir, 'yolov4-tiny.cfg')

# Download the files
def download_file(url, path):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check for errors
    with open(path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Downloaded {url} to {path}")


download_file(weights_url, weights_path)
download_file(cfg_url, cfg_path)
