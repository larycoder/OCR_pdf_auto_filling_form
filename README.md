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
- This version should work well with linux ( but not windows or mac )

## Installation:
- Download [this](https://github.com/larycoder/OCR_pdf_auto_filling_form) repo to your localhost
- CLone [Tesseract](https://github.com/sirfz/tesserocr) to folder with name: tesserocr

## Requirements
###### #python
- Image processing
```
pip install img2pdf opencv matplotlib numpy pdf2img
```
- Handle object storing user properties
```
pip install json
```

###### #java
- This project was built in java 11
with these packages:
```
java.awt javax.swing java.util java.io
```
## Process to run:
### Convert PDF to JPG and put it to folder for handling:
- Put PDF financial form to root of repo.
- From terminal run:
```
./filePrepare $File_PDF
```
file **filePrepare** has function to generate New folder in direction templates/ with the name is name of PDF file. In that folder will have many subfolder equal to 1 page PDF. As PDF file has many pages then each page will be convert to 1 image jpg and put to the subfolder mention above.

### Create template for each Image on each subfolder:

###### **Note: for multiple pages PDF file, you will need to repeat these steps multiple times for each subdirection.**

- From terminal run:
```
./getRecPos templates/$PDF_file_dir/$sub_PDF_file_dir
```
When running this fife, you will recieve 1 form of image to navigate position of fields. First you navigate field of words then navigate blank to fill of that field. You can navigate by right click on 1 point, hold click and move to the next point then release click which will define 1 rectangle -> position of this rect will be saved for next step. After done all navigation, press C to save and exit. 

Then you can go to **PDF_name_rect_pos.txt** on subdirection that you define in code to check all position with pair of line equal to position field and position blank.

- Building field of words in text form:
```
./getFieldName templates/$PDF_dir/$subPDF_dir
```
This function will catch all image that you was navigated that include word and translate them upon text saving on file: **field_name.txt** in the folder which you has already presented in code.

Right now, because the translate image to code depend on tesserocr which can has some error on detecting and translating. You need to do this stuff by hand:

**Rules of field_name.txt file:**
1. Each words field navigating in previous step need to layout in only 1 line.
2. The order of words in file must corresponding to the order of words field when you navigated in image upon previous step.

Then, checking and making sure all file field_name.txt on all subfolder are correct before going to next step.

- Build template for PDF form:
```
./buildTemplate templates/$PDF_dir_want_to_build
```

This function will go throw all subdirection of PDF direction, reading all position file, field_name file and depending on those file to create 1 dictionary hold all information needed in kind of json file. You can check that file in **template.json** in each subdirection of PDF folder.

### Request user value and return it back to PDF file.

- Run in terminal:
```
./exportPDF templates/$PDF_file_dir
```

By running this script: the function will go throw all subdirectory of PDF folder and create GUI to ask user input their value then put all that info to user.json Which will be using to insert user information to PDF form. This process will run multiple times depend on number of subdirectory of PDF folder -> there will be multiple windows show and ask user to insert their info.

###### **you can check final result in PDF file holded on PDF folder with name equal to PDF file you put in first step.**
