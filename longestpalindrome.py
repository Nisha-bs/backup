# sen = "cdaaabcaca"
# newlist = []
# lenlist = []
# min = 0
# maxpalin = ""
# for i in range(len(sen)):
#     for j in range(len(sen)):
#         word = sen[i:j+1]
#         if (word == word[::-1] and word != ""):
#             if (min < len(word)):
#                 min = len(word)
#                 maxpalin = word
#         else:
#             pass
# print(maxpalin)

# pointer method
sen = "daaaab"
i = 0
j = 0
palin = ""
while (j < len(sen)):
    print(i)
    word = sen[i:j + 1]
    print(i, j, word)
    if (word == word[::-1] and i != j):
        palin = word
        i = i + 1
        print(word)

    elif (j == i):
        j = j + 1

print(palin)
