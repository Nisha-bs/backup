# import itertools
# input_string = "abcdACeDzoedaccc"
# vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# occur = {}
# for char in input_string:
#     # print(char)
#     if (char in vowels):
#         print(f"vowels {char}")
#         if (char in occur):
#             occur[char] += 1
#         else:
#             occur[char] = 1

#     else:
#         continue
# print(f"frequency {occur}")


# print(list(itertools.combinations(input_string,)))

input_string = "abbcbcpc"
start = 0
end = 1
count = 1
char = None
high = 0
while True:
    print("start end", start, end, input_string[start], input_string[end])
    if (input_string[start] == input_string[end]):
        # print(input_string[start], input_string[end])
        end += 1
        count += 1
        print("yes", count, end)
    elif (input_string[start] == input_string[end]) and (end == len(input_string)) and (high < count):
        high = count
        char = input_string[start]
        # print(high)
    elif (input_string[start] == input_string[end]) and (end == len(input_string)) and (high > count):
        # print(high)
        # char = input_string[start]
        # print(char)
        break

    else:
        # print(count, char)
        if (count == 1):
            high = 1
            char = input_string[start]
            # print(input_string[start], input_string[end])
            # print("count", count, char, high)

        elif (count > 1) and (high < (count)):
            high = count
            count = 1
            char = input_string[start]
            print(count, char)
            # print(input_string[start], input_string[end])
            print("count1", high)
        start = end
        end = end + 1
    if (end >= len(input_string)):
        char = input_string[start]
        if (high < count):
            high = count
        print(char, high)
        break
