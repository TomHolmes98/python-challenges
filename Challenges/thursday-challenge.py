def chall(phrase):
    phrase_splitted = phrase.split(' ')
    word_list = []
    for i in phrase_splitted:
        if i not in word_list:
            word_list.append(i)
        else:
            continue
    word_list.sort()
    return((' ').join(word_list))

print(chall('hello world and practice makes perfect and hello world again'))



