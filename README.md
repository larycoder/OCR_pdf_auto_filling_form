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
