#previous_row_comaprison_newcol_value_assigned
"""
********* INPUT **************
Name	Age	subject	  marks	ID
Ankit	25	science	  80	   1
Ankit	25	social	  70	   1
Anuj	26	maths	    90	   2
Anuj	26	english	  80	   2
Anil	27	sanskrit	70	   3
Ram	  28	maths	    60	   4
shyam	29	hindi	    70	   5
mohan	30	english	  80	   6

********* OUTPUT **************
Name	Age	subject	 marks	ID	new
Ankit	25	science	  80	  1	  80
Ankit	25	social	  70	  1	  150
Anuj	26	maths	    90	  2	  90
Anuj	26	english	  80	  2	  170
Anil	27	sanskrit	70	  3	  70
Ram	  28	maths	    60	  4	  60
shyam	29	hindi	    70	  5	  70
mohan	30	english	  80	  6	  80
"""
# CODE: --------------------------------------------------------------------------------------------------
import pandas as pd
data = pd.read_excel("/home/deepu/Downloads/prob.xlsx")
df = pd.DataFrame(data)
a = df['ID']
b = df['marks']
df['new'] = df['marks']
c = df['new']
aLen = len(a)
for i, j in enumerate(a):
    if i != (aLen-1):
        if a[i+1] == a[i]:
            #c[i] = b[i]
            c[i+1] = c[i]+c[i+1]
        else:
            c[i+1] = b[i+1]
    else:
        pass
print(df)
