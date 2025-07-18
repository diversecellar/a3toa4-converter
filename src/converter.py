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
from pathlib import Path

fixed_code_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(fixed_code_path)

from tkinter import Tk
from tkinter import Button
from tkinter import filedialog
root = Tk()
# root.withdraw()
filename = filedialog.askdirectory(title="Select Folder With A3 Scans")
# def open():

#     print(filename)
# button = Button(root, text="Open A3 Scans Folder", command=open)
# button.pack()
root.destroy()
code_path = os.path.join(filename)
code_path = Path(code_path).as_posix()
os.chdir(code_path)
scans_dir = os.getcwd()
output_folder_name = str(os.path.basename(code_path)) + " - A4 Outputs"
parent_dir = os.path.dirname(code_path)
list_of_files = glob.glob("*.pdf", recursive=False)
os.chdir(code_path)

print("-----------------------------------------------------")
print("START: processing scans! - from {} for inputs".format(scans_dir))
print("-----------------A3 to A4 Converter------------------")

def a3_to_two_a4(input_pdf_path, output_pdf_path):
    """
    Converts an A3 PDF page into two A4 pages (left and right halves).

    Args:
        input_pdf_path (str): Path to the input A3 PDF file.
        output_pdf_path (str): Path to save the output PDF file with A4 pages.
    """
    os.chdir(code_path)
    doc = pymupdf.open(input_pdf_path)
    new_doc = pymupdf.open()

    a3_width, a3_height = pymupdf.paper_size("a3-L") # Get A3 dimensions in points
    a4_width, a4_height = pymupdf.paper_size("a4") # Get A4 dimensions in points

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_width = page.rect.width
        page_height = page.rect.height

        # Calculate the split point for A4 pages
        split_x = page_width / 2
        # Create the left A4 page
        rect_left = pymupdf.Rect(0, split_x, page_height, page_width)
        while page.number != 0:
            new_page_left = new_doc.new_page(width=page_height, height=split_x)
            new_page_left.show_pdf_page(new_page_left.rect, doc, page.number, clip=rect_left)
            new_page_left.set_rotation(90)
            break
        # Create the right A4 page
        rect_right = pymupdf.Rect(0, 0, page_height, split_x)
        new_page_right = new_doc.new_page(width=page_height, height=split_x)
        new_page_right.show_pdf_page(new_page_right.rect, doc, page.number, clip=rect_right)
        new_page_right.set_rotation(90)
        #new_page_left.draw_rect(rect_left, color=(1, 0, 0), fill=(0, 0, 1), width=2)

        # # Create the right A4 page
        # rect_right = pymupdf.Rect(split_x, 0, page_width, page_height)
        # new_page_right = new_doc.new_page(width=split_x, height=page_height)
        # new_page_right.show_pdf_page(new_page_right.rect, doc, page.number, clip=rect_right)

        # # Revert page rotation if it was changed
        # if page.rotation in {90, 270} and (a3_width, a3_height) != (temp_width, temp_height):
        #     page.set_rotation(0) # Revert rotation

    if not os.path.exists(output_folder_name):
        os.mkdir(output_folder_name)
    os.chdir(output_folder_name)
    new_doc.save(output_pdf_path)
    new_doc.close()
    doc.close()
    os.chdir(code_path)

# usage:


outs_dir = os.path.join(code_path, output_folder_name)
outs_dir = Path(outs_dir).as_posix()
for file in list_of_files:
    scans = os.path.join(code_path, file)
    scans = Path(code_path).as_posix()
    outs = os.path.join(outs_dir, file)
    print("PROCESS: processing a3 file", scans)
    a3_to_two_a4("{}".format(file), "{}".format(file))
    #print("END: done converting a3 file to a4:", outs)
print("-----------------------------------------------------")
print("DONE: finished processing scans - check {} for outputs".format(outs_dir))
print("END: now opening output folder {} in windows file explorer".format(outs_dir))
os.startfile(outs_dir)
print("-----------------------------------------------------")