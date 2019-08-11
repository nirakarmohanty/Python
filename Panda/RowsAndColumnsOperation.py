import pandas as pd
import xlrd

movie_df = pd.read_csv('E:\Python\Panda\movie.csv')

print("Print Shape of the table :",movie_df.shape)
rows,columns=movie_df.shape
print("Print rows {} and columns {}".format(rows,columns))

print("Head values",movie_df.head())

print("Tail values",movie_df.tail())

print("Head values for some rows ", movie_df.head(2))
print("Tail values for some rows ", movie_df.tail(2))

print("Movies Data ",movie_df[1:10])

print("Only Movie Title name",movie_df.movie_title[0:3])
print("Only Movie Title name",movie_df['movie_title'][0:3])

print("==========Print only some columns=========")
print(movie_df[['movie_title','num_user_for_reviews']][0:3])
