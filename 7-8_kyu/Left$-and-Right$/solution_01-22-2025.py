def left(string,i=1):
    if isinstance(i, int):
        return string[:i]
    if isinstance(i, str):
        return string.split(i)[0]
    
def right(string,i=1):
    if isinstance(i, int):
        return string[-i:len(string)] if i != 0 else ''
    if isinstance(i, str):
        return string.split(i)[-1]