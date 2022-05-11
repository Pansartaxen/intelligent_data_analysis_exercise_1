def hashtagExtraction(text):
    text = text.split(' ')
    output = []
    punctuations = ['.', ',', '!', '?', ';', ':']
    for i in text:
        if i[0] == '#':
            if i[-1] in punctuations:
                i = i[:-1:]
            output.append(i)
    return(output)