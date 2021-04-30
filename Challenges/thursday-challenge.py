def chall(phrase):
    split_phrase = phrase.split(' ')
    word_list = []
    for i in split_phrase:
        if i not in word_list:
            word_list.append(i)
        else:
            continue
    word_list.sort()
    return((' ').join(word_list))

print(chall('hello world and practice makes perfect and hello world again'))




