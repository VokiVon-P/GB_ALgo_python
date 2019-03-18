__author__ = 'Павел Новиков (aka VokiVon)'

"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import collections

cnt_ = collections.Counter("мама мыла раму")
print(cnt_)

for i in cnt_.keys():
    print(i)
    print(cnt_[i])




