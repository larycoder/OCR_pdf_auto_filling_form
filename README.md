# Youtube video links:
https://youtu.be/G-8ZZo8lD8Y

# Ideas
* Financial form may not changes frequently
* With each form, we save the template and reuse
* Template generation should done manually but only the first time
* If we meet the form that already have template, just use it
# Process to make template
* Convert PDF -> img (pdf2img in python)
* Mark the position of field and blanks (openCV)
* Create template and save in JSON file (python)
* Ask user input for blank values (java GUI)
* write information to img (openCV)
* img -> PDF (img2pdf)

**For the form that already has template, just parse the JSON and ask for input**

**Checkbox and table are not handled in this version yet**


# First step to work:
- It should work well with linux ( but not windows or mac )

## Installation:
- Download repo to your localhost
- CLone [Tesseract](https://github.com/sirfz/tesserocr) to my repo with name: tesserocr
- Install python librery with pip: Pillow, numpy, opencv-python, matplotlib, pytesseract, img2pdf, pdf2img, v.v. ( install more if lack )

## Process to run:
- Put PDF file want to work to root of repo.
- In ImageProcess.py: comment which not is function and run only convertPdf2Jpg(Path_to_file_of_PDF)
- Now, you should have all image converted from your PDF: somekind like: name_of_pdf + some_number + jpg
- Then you will have 1 shell script file "dirPrepare.sh" for creating the direction
