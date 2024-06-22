'''''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать
без get_dummies?

'''''



import random
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

encode = OneHotEncoder(handle_unknown='ignore')
encode_df = pd.DataFrame(encode.fit_transform(data[['whoAmI']]).toarray()).astype(int)
final_df = data.join(encode_df)
final_df.drop(final_df[[0]], axis= 1 , inplace= True )
final_df.rename(columns={1: 'lst'}, inplace=True)
print(final_df.head())