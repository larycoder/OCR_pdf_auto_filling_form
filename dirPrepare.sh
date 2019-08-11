#!/usr/bin/bash

dir=./templates
form=$1
num=$2


if [ ! -d $dir ]; 
  then mkdir $dir;
fi

dir=$dir'/'$form;

if [ ! -d $dir ];
  then mkdir $dir;
fi

dir=$dir'/'$form$num;

if [ ! -d $dir ];
  then mkdir $dir;
fi

temp=$dir'/field'

if [ ! -d $temp ];
  then mkdir $temp;
fi

temp=$dir'/field_name.txt'

if [ ! -f $temp ];
  then touch $temp
fi

temp=$dir'/template.json'

if [ ! -f $temp ];
  then touch $temp
fi

temp=$dir'/user.json'

if [ ! -f $temp ];
  then touch $temp
fi

temp=$dir'/'$form'_rect_pos'.txt

if [ ! -f $temp ];
  then touch $temp
fi

