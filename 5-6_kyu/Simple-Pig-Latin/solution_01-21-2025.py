def pig_it(text):
    result = []
    for word in text.split(" "):
        result.append(word[1:] + word[0] + "ay") if word not in ",.?!" else result.append(word)
    return " ".join(result)