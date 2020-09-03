test_string = input("What is the string you want to test?\n>>> ")
words = test_string.split(" ")
word_counter = {}
for word in words:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

words = list(word_counter.keys())
words.sort()

for word in words:
    print("{} - {}".format(word, word_counter[word]))

