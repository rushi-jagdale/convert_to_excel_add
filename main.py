import os
import pandas as pd
path = []
for root, dirs,files in os.walk('/home/sarth/anaconda3/c360/convertingfile'):
    for file in files:
        if file.endswith('.csv'):
            s = os.path.join(root,file)

            path.append(s)
for file in path:
    df = pd.read_csv(file)