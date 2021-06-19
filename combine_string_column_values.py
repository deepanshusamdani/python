#ref: https://www.kite.com/python/answers/how-to-combine-string-column-values-in-a-pandas-dataframe-using-groupby-in-python
Column1 Column2
0        1       A
1        2       B
2        2       C
3        1       D
4        3       E

grouped_df = df.groupby("Column1")

grouped_lists = grouped_df["Column2"].agg(lambda column: "".join(column))

grouped_lists = grouped_lists.reset_index(name="Column2")

print(grouped_lists)
OUTPUT
   Column1 Column2
0        1      AD
1        2      BC
2        3       E
