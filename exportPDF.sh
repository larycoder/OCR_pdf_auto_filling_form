#!/usr/bin/bash

NUM='2'

# java test "templates/SOK/SOK$NUM/field_name.txt"
# python ObjectHandle.py --mode '2' --user_value user_value.txt --input_template templates/SOK/SOK$NUM/template.json --user_json templates/SOK/SOK$NUM/user.json --file_name templates/SOK/SOK$NUM/field_name.txt --position templates/SOK/SOK$NUM/SOK$NUM"_rect_pos".txt --output_template templates/SOK/SOK$NUM/template.json
# python ObjectHandle.py --mode '1' --user_value user_value.txt --input_template templates/SOK/SOK$NUM/template.json --user_json templates/SOK/SOK$NUM/user.json --file_name templates/SOK/SOK$NUM/field_name.txt --position templates/SOK/SOK$NUM/SOK$NUM"_rect_pos".txt --output_template templates/SOK/SOK$NUM/template.json


# python ImgGen.py --template templates/SOK/SOK$NUM/user.json --output templates/SOK/$NUM.jpg --input templates/SOK/SOK$NUM/SOK$NUM.jpg
# python GetPdf.py --directory templates/SOK --output SOK.pdf


python GetRectPos.py --image templates/SOK/SOK$NUM/SOK$NUM.jpg --output templates/SOK/SOK$NUM/SOK$NUM"_rect_pos".txt