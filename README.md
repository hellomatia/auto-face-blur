# Face Blur

Face Blur is a Python script that automatically detects and blurs faces in images using the MTCNN (Multi-task Cascaded Convolutional Networks) face detection model.

## Prerequisites

Before running this script, ensure you have Python 3.6 or later installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Installation

1. Clone this repository or download the script to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. It's recommended to create a virtual environment:
```
python -m venv venv
```
4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required packages using pip:
```
pip install opencv-python numpy mtcnn
```

## Usage

1. Ensure your virtual environment is activated.

2. Run the script using Python:
```
python face_blur.py
```
3. When prompted, enter the full path to the directory containing the images you want to process.

Example:
```
Enter the path of the directory containing images to process: C:\Users\YourName\Pictures\ToBlur
```

4. The script will process all image files (jpg, jpeg, png, bmp) in the specified directory.

## How it works

1. The script uses the MTCNN model to detect faces in each image.
2. It then applies a Gaussian blur to each detected face region.
3. The processed images are saved in a new directory named "blurred_results" within the input directory.

## Output

- Processed images are saved in a new folder named "blurred_results" within the input directory.
- The original filenames are preserved for the blurred images.
- Console output provides information about each step of the process, including:
- When image processing starts
- Number of faces detected in each image
- When face blurring is completed
- The path where each processed image is saved

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)

## Notes

- Ensure you have the necessary permissions to read from the input directory and write to the output directory.
- The script processes only the images in the specified directory, not in its subdirectories.
- Processing time may vary depending on the number and size of the images, as well as the number of faces in each image.

## Trouble shooting

If you encounter any issues:
- Ensure all required packages are correctly installed.
- Check that the input directory path is correct and accessible.
- Verify that you have write permissions in the input directory to create the "blurred_results" folder.

For any other issues, please open an issue in the GitHub repository.