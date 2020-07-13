file1 = open("doc1.txt", "r")
text1 = file1.read()
text1

file2 = open("doc2.txt", "r")
text2 = file2.read()
text2

str1 = ''.join(text1)
str2 = ''.join(text2)

sent1_text1 = str1.split('.')
sent2_text2 = str2.split('.')


final_list = []
for z in sent1_text1:
    for y in sent2_text2:
        if z == y:
            final_list.append(z)

#Read in the a file
#with file1 = open('doc.txt', 'r')
 #   filedata = file1.read()

#Replace 'the_word' with * 'the_word' * -> "highlight" it
#filedata.replace(the_word,  "*" + the_word + '*')

#Write the file back
#with file1 = open('file.txt', 'w')
 #   file1.write(filedata)

