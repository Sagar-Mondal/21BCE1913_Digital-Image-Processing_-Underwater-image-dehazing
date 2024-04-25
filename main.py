import os
import cv2
import natsort
from LabStretching import lab_stretching
from RGBStretching import rgb_stretching

def process_image(input_folder, output_folder):
    files = os.listdir(input_folder)
    files = natsort.natsorted(files)

    for file in files:
        input_filepath = os.path.join(input_folder, file)
        if os.path.isfile(input_filepath):
            img = cv2.imread(input_filepath)

            img = rgb_stretching(img)
            img = lab_stretching(img)

            output_filepath = os.path.join(output_folder, file)
            cv2.imwrite(output_filepath, img)

if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    raw_folder = os.path.join(current_dir, "dataset", "raw-890")
    results_folder = os.path.join(current_dir, "results")

    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    process_image(raw_folder, results_folder)
