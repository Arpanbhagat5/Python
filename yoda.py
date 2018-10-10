
def pig(word):
    if word[0] in ['a','e','i','o','u']:
        print(word + 'ay')
    else:
        print(word[1:] + word[0] + 'ay')

pig("wabc")