import cv2
import numpy as np
from mtcnn import MTCNN
import os

def blur_face(image, factor=3.0):
    (h, w) = image.shape[:2]
    kW = int(w/factor)
    kH = int(h/factor)
    
    if kW % 2 == 0:
        kW -= 1
    if kH % 2 == 0:
        kH -= 1
    
    return cv2.GaussianBlur(image, (kW, kH), 0)

def process_image(image_path, output_path):
    try:
        print(f"Starting image processing: {image_path}")
        
        # Load MTCNN face detector
        detector = MTCNN()
        print("Face detector loaded successfully")

        # Load image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Unable to load image: {image_path}")
            return

        print("Image loaded successfully")
        
        # Convert to RGB (MTCNN uses RGB images)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect faces
        faces = detector.detect_faces(rgb_image)
        print(f"Number of faces detected: {len(faces)}")

        # Apply blur to each detected face
        for face in faces:
            x, y, w, h = face['box']
            face_region = image[y:y+h, x:x+w]
            face_region = blur_face(face_region)
            image[y:y+h, x:x+w] = face_region

        print("Face blurring completed")

        # Save the result
        cv2.imwrite(output_path, image)
        print(f"Processed image saved: {output_path}")
        
    except Exception as e:
        print(f"Error occurred during image processing: {str(e)}")

def process_directory(input_dir):
    # Create output directory
    output_dir = os.path.join(input_dir, "blurred_results")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']

    # Process only files in the specified folder
    for file in os.listdir(input_dir):
        if any(file.lower().endswith(ext) for ext in image_extensions):
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            process_image(input_path, output_path)

if __name__ == "__main__":
    input_directory = input("Enter the path of the directory containing images to process: ")
    process_directory(input_directory)