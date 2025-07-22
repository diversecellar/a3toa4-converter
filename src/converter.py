# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 10:02:24 2025

@author: Paul Namalomba
"""

import subprocess
import sys
import os
import glob
import pymupdf
import pypdf
from pypdf import PdfReader, PdfWriter, PaperSize
from pathlib import Path
from tkinter import Tk, Button, filedialog, simpledialog

# Stuff that is standard in all my codes (where is .py located essentially)
fixed_code_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(fixed_code_path)

# Create a Tkinter root window, but hide it as it's not needed for filedialog
root = Tk()
# root.withdraw()
# Prompt the user for input using the file explorer to select folder
src_docs_foldername = filedialog.askdirectory(title="Select Folder With A3 Scans")
# def open():

#     print(filename)
# button = Button(root, text="Open A3 Scans Folder", command=open)
# button.pack()
root.destroy() # destroy the TK root window

# Code to store data about the directory containg the source files
src_docs_path = os.path.join(src_docs_foldername) # force parse as path
src_docs_path = Path(src_docs_path).as_posix() # force parse as path in the current OS
os.chdir(src_docs_path) # change to the directory with the source files
scans_dir = os.getcwd() # redudant but perhaps useful
output_folder_name = str(os.path.basename(src_docs_path)) + " - A4 Outputs" # store name of outputs folder directory
parent_dir = os.path.dirname(src_docs_path) # name of parent to src_docs_path
list_of_files = glob.glob("*.pdf", recursive=False) # list of A3 target documents
os.chdir(src_docs_path) # change to the directory with the source files

print("-----------------------------------------------------")
print("START: processing scans! - from {} for inputs".format(scans_dir))
print("-----------------A3 to A4 Converter------------------")

# Create a Tkinter root window, but hide it as it's not needed for simpledialog
root_2 = Tk()
root_2.withdraw()
# Prompt the user for input using a dialog box
user_input = simpledialog.askstring(title="User Input",
                                    prompt="Please specify whech side of the A3 page is the first page of your output document (L or R):")
user_input = str(user_input) # force string

# Check if the user entered something or clicked Cancel
if user_input is not None:
    if user_input.lower()[:1] == "l": # if user puts in "left", "LeFT" or "l" will be  a positive catch
        print("PROCESS: left-side (in landscape) is first page")
    else:
        print("PROCESS: right-side (in landscape) is first page")
else:
    print("END: User cancelled the input or entered no input.")
    sys.exit() # exit function to stop the run

def a3_to_two_a4(input_pdf_path, output_pdf_path):
    """
    Converts an A3 PDF page into two A4 pages (left and right halves).

    Args:
        input_pdf_path (str): Path to the input A3 PDF file.
        output_pdf_path (str): Path to save the output PDF file with A4 pages.
    """
    os.chdir(src_docs_path) # change to the directory with the source files
    doc = PdfReader(input_pdf_path)
    writer = PdfWriter()

    a4_width = PaperSize.A4.width
    a4_height = PaperSize.A4.height

    for page_num, page in enumerate(doc.pages):
        # Ensure the page is A3 landscape (approximate check)
        # A3 landscape dimensions: ~1191 x 842 points (72 dpi)
        # A4 portrait dimensions: ~595 x 842 points (72 dpi)
        # So A3 landscape is essentially (2 * A4_width) x A4_height

        rotated_angle = page.rotation
        page_width = float(page.mediabox.height)
        page_height = float(page.mediabox.width)

        if rotated_angle in [0, 180]:
            if str(user_input).lower() == "r":
                while page_num >= 1:
                    # Create the first A4 page (left half of the A3)
                    left_half = writer.add_blank_page(width=a4_width, height=a4_height)
                    # Set the crop box to the left half of the A3 page
                    left_half.mediabox.lower_left = (0, 0)
                    left_half.mediabox.upper_right = (page_width / 2, page_height)

                    # Add the content of the original page to the new A4 page
                    # The .add_transformation() is crucial for positioning the content correctly
                    left_half.add_transformation((1, 0, 0, 1, 0, 0)) # No transformation for the left half
                    left_half.merge_page(page)
                    left_half.rotate(rotated_angle)
                    break
            else:
                # Create the first A4 page (left half of the A3)
                left_half = writer.add_blank_page(width=a4_width, height=a4_height)
                # Set the crop box to the left half of the A3 page
                left_half.mediabox.lower_left = (0, 0)
                left_half.mediabox.upper_right = (page_width / 2, page_height)

                # Add the content of the original page to the new A4 page
                # The .add_transformation() is crucial for positioning the content correctly
                left_half.add_transformation((1, 0, 0, 1, 0, 0)) # No transformation for the left half
                left_half.merge_page(page)
                left_half.rotate(rotated_angle)

            # Create the second A4 page (right half of the A3)
            right_half = writer.add_blank_page(width=a4_width, height=a4_height)
            # Set the crop box to the right half of the A3 page
            right_half.mediabox.lower_left = (page_width / 2, 0)
            right_half.mediabox.upper_right = (page_width, page_height)

            # Translate the content of the original page to fit the right A4 page
            # We shift the content left by half the A3 width
            right_half.add_transformation((1, 0, 0, 1, -page_width / 2, 0))
            right_half.merge_page(page)
            right_half.rotate(rotated_angle)

        else:
            if str(user_input).lower() == "r":
                while page_num >= 1:
                    # Create the first A4 page (left half of the A3)
                    left_half = writer.add_blank_page(width=a4_width, height=a4_height)
                    # Set the crop box to the left half of the A3 page
                    left_half.mediabox.lower_left = (0, 0)
                    left_half.mediabox.upper_right = (page_height, page_width / 2)

                    # Add the content of the original page to the new A4 page
                    # The .add_transformation() is crucial for positioning the content correctly
                    left_half.add_transformation((1, 0, 0, 1, 0, 0)) # No transformation for the left half
                    left_half.merge_page(page)
                    left_half.rotate(rotated_angle)
                    break
            else:
                # Create the first A4 page (left half of the A3)
                left_half = writer.add_blank_page(width=a4_width, height=a4_height)
                # Set the crop box to the left half of the A3 page
                left_half.mediabox.lower_left = (0, 0)
                left_half.mediabox.upper_right = (page_height, page_width / 2)

                # Add the content of the original page to the new A4 page
                # The .add_transformation() is crucial for positioning the content correctly
                left_half.add_transformation((1, 0, 0, 1, 0, 0)) # No transformation for the left half
                left_half.merge_page(page)
                left_half.rotate(rotated_angle)

            # Create the second A4 page (right half of the A3)
            right_half = writer.add_blank_page(width=a4_width, height=a4_height)
            # Set the crop box to the right half of the A3 page
            right_half.mediabox.lower_left = (0, page_width / 2)
            right_half.mediabox.upper_right = (page_height, page_width)

            # Translate the content of the original page to fit the right A4 page
            # We shift the content left by half the A3 width
            right_half.add_transformation((1, 0, 0, 1, -page_height / 2, 0))
            right_half.merge_page(page)
            right_half.rotate(rotated_angle)

    if not os.path.exists(output_folder_name):
        os.mkdir(output_folder_name)
    os.chdir(output_folder_name)
    with open(output_pdf_path, "wb") as output_stream:
        writer.write(output_stream)
    os.chdir(src_docs_path) # change back to the directory with the source files

# Usage:
output_dir = os.path.join(src_docs_path, output_folder_name) # parse as path the output folder directory
output_dir = Path(output_dir).as_posix() # force parse as path in the current OS

# loops over all files in the list of A3 target source documents
for file in list_of_files:
    src_scan_file = os.path.join(src_docs_path, file) # parse as path the source file
    src_scan_file = Path(src_scan_file).as_posix() # force parse as path in the current OS
    output_pdf_file = os.path.join(output_dir, file) # parse as path the output file
    print("PROCESS: processing a3 file", src_scan_file)
    a3_to_two_a4("{}".format(file), "{}".format(file))
    #print("END: done converting a3 file to a4:", outs)
print("-----------------------------------------------------")
print("DONE: finished processing scans - check {} for outputs".format(output_dir))
print("END: now opening output folder {} in windows file explorer".format(output_dir))
os.startfile(output_dir)
print("-----------------------------------------------------")