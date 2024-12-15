def ops(str):
    words=str.split()
    print("No of word: ",len(words))
    longest_word=max(words, key=len) if words else None
    print("Largest word: ",longest_word)
    numeric_words = [word for word in words if word.isdigit()]
    print(numeric_words)

str=input("enter the string:\n")
ops(str)