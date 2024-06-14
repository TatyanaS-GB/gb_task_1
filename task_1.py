"""В ячейке ниже представлен код генерирующий DataFrame, которая состоит
всего из 1 столбца. Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()"""
import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

data.head()


one_hot = pd.DataFrame()

one_hot['robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
one_hot['human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)

print(one_hot.head())