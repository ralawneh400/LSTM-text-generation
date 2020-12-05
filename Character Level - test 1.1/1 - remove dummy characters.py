import string


filename = "men_in_the_sun.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()

raw_text = raw_text.replace("", " ")
raw_text = raw_text.replace("»", " ")
raw_text = raw_text.replace("..", " ")
raw_text = raw_text.replace(".", " ")
raw_text = raw_text.replace("|", " ")
raw_text = raw_text.replace("\"", " ")
raw_text = raw_text.replace(")", " ")
raw_text = raw_text.replace("(", " ")
raw_text = raw_text.replace("«", " ")
raw_text = raw_text.replace("\t", " ")


print(raw_text)

f = open("men_in_the_sun_edited.txt", "w", encoding='utf-8')
f.write(raw_text)
f.close()
