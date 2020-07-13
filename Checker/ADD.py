sentence = 'My name is Lyba'
split_value = []
tmp = ','
c = '\0'
for c  in sentence:

    if c == '':
        print("hi im in")
        split_value.append(tmp)
        tmp = ','
    else:
        tmp += c
        if tmp:
            split_value.append(tmp)
print(sentence)
