:: Create a folder called new_folder first

mkdir new_folder

:: Create folder called if_folder using if command

::if exist new_folder mkdir if_folder

:: Using if else statement to create folders caller hyperionDev or new-projects

if exist if_folder ( mkdir hyperionDev)  else ( mkdir new-projects)