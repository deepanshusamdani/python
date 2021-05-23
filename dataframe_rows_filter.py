"""
Created on Sunday

@author: deepu
"""

import pandas as pd
import numpy as np

raw_data = {'student':['A','B','C','D','E'],
        'score': [100, 96, 80, 105,156], 
    'height': [7, 4,9,5,3],
    'trigger1' : [84,95,15,78,16],
    'trigger2' : [99,110,30,93,31],
    'trigger3' : [114,125,45,108,46]}

df = pd.DataFrame(raw_data)
print(df)

def text_df(df):

    if (df['trigger1'] <= df['score'] < df['trigger2']) and (df['height'] < 8):
        return "Red"    
    elif (df['trigger2'] <= df['score'] < df['trigger3']) and (df['height'] < 8):
        return "Yellow"
    elif (df['trigger3'] <= df['score']) and (df['height'] < 8):
        return "Orange"
    elif (df['height'] > 8):
        return np.nan
    
df['Flag'] = df.apply(text_df, axis = 1)
df['t1Flag'] = df['trigger1'].apply(lambda x: 'True' if x >= 75 and x <=85 else 'False')
df['t2Flag'] = df['trigger2'].apply(lambda x: 'True' if x >= 90 else 'False')
df[(df.t1Flag == "True") & (df.t2Flag == "True")]
print(df)


#alternate method of above logic to filterout the rows from datframe
lis = ['A','D']
aDf = df[(df.trigger1 >= 75) & (df.trigger1<= 85) & (df.student.isin(lis))]
print(df)
