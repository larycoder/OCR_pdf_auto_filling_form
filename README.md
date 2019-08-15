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
## Process to run:
### Convert PDF to JPG and put it to folder for handling:
- Put PDF financial form to root of repo.
- From terminal run:
```
./filePrepare $Name_of_PDF
```
file **filePrepare** has function to generate New folder in direction templates/ with the name is name of PDF file. In that folder will have many subfolder equal to 1 page PDF. As PDF file has many pages then each page will be convert to 1 image jpg and put to the subfolder mention above.

### Create template for each Image on each subfolder:

###### **Note: for multiple pages PDF file, you will need to repeat these steps multiple times for each subdirection.**

- From terminal run:
```
python GetRecPos.py --image templates/$PDF_dir/$subPDF_dir/*.jpg --output templates/$PDF_dir/$subPDF_dir/*_rect_pos.txt
```
When running this life, you will recieve 1 form of image to navigate position of fields. First you navigate field of words then navigate blank to fill of that field. You can navigate by click on 1 point then move to the next point and click again. After done all navigation, press C to save and exit. 
Then you can go to **PDF_name_rect_pos.txt** to check all position with pair of line equal to position field and position blank.

- Building field of words in text form:
```
./getFieldName templates/$PDF_dir/$subPDF_dir
```
This function will cat all image that you was navigated that include word and translate them on text saving on file: **field_name.txt** in the folder which you has already presented in code.

Right now, because the translate image to code depend on tesserocr which can has some error on detecting and translating. You need to do this stuff by hand:

**Rules of field_name.txt file:**
1. Each words field navigating in previous step need to layout in only 1 line.
2. The order of words in file must corresponding to the order of words field when you navigate in image upon previous step.

Then, checking and making sure all file field_name.txt on all subfolder are correct before go to next step.

- 