# image_process.py

import cv2
import os
import insightface
from insightface.app import FaceAnalysis

# Initialize the models once when the app starts
def initialize_models():
    """Initializes and returns the InsightFace models."""
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))
    # Correcting the model file path using double backslashes for Windows compatibility
    swapper =insightface.model_zoo.get_model('inswapper_128.onnx',download=False,download_zip=False)
    return app, swapper

def process_images_for_swap(image1_path, image2_path, app, swapper):
    """
    Takes two image paths, swaps faces, and saves the output images.
    Returns the paths to the saved output images.
    """
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Detect faces
    face1 = app.get(img1)
    face2 = app.get(img2)

    if not face1 or not face2:
        return None, None # Return None if a face isn't detected

    # The swapper expects the first face it finds
    result_img1 = swapper.get(img1, face1[0], face2[0], paste_back=True)
    result_img2 = swapper.get(img2, face2[0], face1[0], paste_back=True)

    # Define paths to save the results
    # Using forward slashes or os.path.join is best practice
    output_path1 = f"static/results/swapped_{os.path.basename(image1_path)}"
    output_path2 = f"static/results/swapped_{os.path.basename(image2_path)}"

    # Save the processed images
    cv2.imwrite(output_path1, result_img1)
    cv2.imwrite(output_path2, result_img2)

    return output_path1, output_path2
