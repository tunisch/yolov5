import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def display_images(image_folder):
    """
    Displays all .jpg images in a specified folder.
    Args:
        image_folder (str): Path to the folder containing images.
    """
    # List all files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

    if not image_files:
        print("No .jpg images found in the folder.")
        return

    # Display each image
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = mpimg.imread(image_path)
        plt.figure(figsize=(10, 5))
        plt.imshow(img)
        plt.title(image_file)
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    # Path to your folder containing images
    image_folder = "C:\\Users\\tunah\\yolov5\\runs\\val\\exp"  # Update this path based on your directory structure
    display_images(image_folder)