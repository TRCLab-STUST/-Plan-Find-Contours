# Organ Contours Finder
This project is to find the skin of the human body from the picture, so as to align and offset the picture later.


## Description of files and dirs
|                |Description                       |Type                         |
|----------------|----------------------------------|-----------------------------|
|Images          |Place a picture of the human body |Resources Dir                |
|Json            |Json File Export                  |Resources Dir                |
|src             |Place Code                        |Sources Dir                  |
|th_out          |Picture after drawing the contours|Resources Dir                |
|src/main.py     |Code                              |Python File                  |

## How to use?
First, put all of you want to find contours' image into `Images Dir`, and run Python file (`main.py`).
It will read images where in the `Images Dir` to run process of `findContours`. Than you can get Json file
and picture after drawing the contours.

## Process of findContours
This processing method in main.py is named `find_c`.
`find_c` needs to pass in arguments (parameters: image, files).  
findContours step:  
  1. First, turn image **BGR to Gray scale**.
  2. gray scale image use **Threshold** to do **Binarization**.
  3. Than, find contours use `OpenCV` method.
  4. Draw　contours and export image.
