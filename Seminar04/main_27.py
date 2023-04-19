# Задача №27. 
# Решение в группах Пользователь вводит текст(строка). Словом считается последовательность 
# непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте. 
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells 
# Output: 13

import string

str_split = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
str_split = str_split.lower() # to avoid counting upper/lower case as 2 different letters

for ch in string.punctuation:
    if ch != '\'':# exeption for ' -> otherwise "I'm" turns into two words
        str_split = str_split.replace(ch, ' ')

str_split = str_split.split()

str_cnt = set(str_split)#it is easier, just unique members of a set!!
print(str_cnt)
print(f"Number of words in the text is: {len(str_cnt)}")


#------> or just DICTIONARY
#str_split = input("Enter some text: ").lower().split()
#str_cnt = {}

# for i in str_split:
#     str_cnt[i] = str_cnt.get(i, 0) + 1
#print(f"Number of words in the text is: {sum(str_cnt)}")