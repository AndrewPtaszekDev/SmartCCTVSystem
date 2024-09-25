# SmartCCTVSystem
This project is a Smart CCTV System that automates the detection and saving of video clips of human movements, optimizing storage efficiency. It leverages computer vision techniques to identify and track people in video frames.

## Features

- Validates input and output paths, ensuring directories exist and handling errors gracefully.
- Uses OpenCV for background subtraction to process video frames, denoise images, and retain significant components.
- Detects and tracks objects using YOLOv4-tiny and OpenCV's MultiTracker, focusing on people.
- Saves video clips when continuous changes are detected, optimizing storage usage.
## Setup

Clone this repository:
~~~
git clone https://github.com/VenaFL/SmartCCTVProject.git 
cd SmartCCTVProject
~~~
Install the required packages:
~~~
pip install -r requirements.txt
~~~
Download the required  weights and configuration files:
 ~~~
 python downloadYOLOFiles.py 
~~~
> Ensure you have the YOLOv4-tiny weights and configuration files in the appropriate directory.

## Usage

**Set Input and Output Paths**:
Define the input path for the video frames or video file, and the output folder for saving clips.
> Ensure these paths are not empty or whitespace.

**Run the code cells**:
Run the *Frame-by-frame capture* or *Video capture* cell depending on your input footage type
 
**Adjust Parameters**:

You can adjust parameters such as minClipLength, minComponentSize, trackingFrames, and trackingBboxScaleFactor to fine-tune detection and tracking performance.

Parameters:
- minClipLength: Minimum length of a video clip to be saved.
- minComponentSize: Minimum size of a connected component to be detected
	> Increasing the minComponentSize can be helpful if the footage has high background noise, such as swaying branches and leaves
- trackingFrames: Number of frames to track an object before re-detection.
	> Decrease trackingFrames for better accuracy, increase it for better performance
- trackingBboxScaleFactor: Scale factor for the bounding box during tracking.


**Monitor Output**:

The processed video clips will be saved in the specified output folder, with frames annotated to show detected objects.

## Notes

Press the 'Esc' key to stop the video processing and close the display window.


## Acknowledgments

- This project uses the YOLOv4-tiny model for object detection.

- Thanks to the OpenCV and CVlib communities for providing powerful computer vision tools.
