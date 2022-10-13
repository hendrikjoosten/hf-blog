from ctypes import sizeof
import numpy as np
import pandas as pd
import markdown
from bs4 import BeautifulSoup
import os


file_list = []
file_list = os.listdir('./md')
real_stuff = []

df = pd.DataFrame()

for fn in file_list:
    html = markdown.markdown(open("./md/" + fn).read())
    text_set = BeautifulSoup(html,features="html.parser").findAll(text=True)
    df


    for i in range(len(text_set)):
        if text_set[i] != '\n':
            real_stuff.append(str(text_set[i]))

print(len(real_stuff))









