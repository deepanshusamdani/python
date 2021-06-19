#Pandas pivot with duplicates [duplicate]
#ref: https://stackoverflow.com/questions/55463459/pandas-pivot-with-duplicates

d = pd.DataFrame({'name': ['Adam', 'Adam', 'Bob', 'Bob', 'Craig'],
              'number': [111, 222, 333, 444, 555], 
              'type': ['phone', 'fax', 'phone', 'phone', 'fax']})

p = d.pivot(index='name', columns = 'type', values='number').reset_index()

#output: ValueError: Index contains duplicate entries, cannot reshape

#alternative way.....
d['key']=d.groupby(['name','type']).cumcount()
p = d.pivot_table(index=['key','name'], columns = 'type', values='number',aggfunc='sum').reset_index()
print(p)
