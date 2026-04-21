def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point?  words = ['this', 'is', 'confusing', 'code', 'AVOID', 'SUCH.']
         # What are the values of first and second at this point? first = ['this', 'is', 'confusing', 'code', 'AVOID', 'SUCH.'], second = ['this', 'is', 'confusing', 'code', 'AVOID', 'SUCH.']
         # What happened? the words "Avoid" and "such." got added to the list and the function made them all caps
print(words)