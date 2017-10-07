FROM armhf/python:3.5
ADD my_script.py /
CMD [ "python", "./my_script.py" ]
