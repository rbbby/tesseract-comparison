import numpy as np
import pandas as pd
import os
import re

os.chdir('/home/robinsaberi/Git_Repos/Tesseract/annotated_newspaper_data/manual_content')

data = np.loadtxt('real_date.txt', delimiter=',', dtype=str)

# Maybe make non-names ints?
def stringExtract(string):
    name, _, txt = string.partition('_')
    edition, page, paragraph = re.findall(r'\d+', txt)[:3]
    return(name, edition, page, paragraph)

real_date_fixed = pd.DataFrame(list(map(stringExtract, data)))
real_date_fixed.columns = ['name','edition','page','paragraph']

real_date_fixed.to_csv('real_date_fixed.csv', index=False)