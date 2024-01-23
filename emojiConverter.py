message = input("> ")
words = message.split(" ")
mp  = {
    ":)" : "😀",
    ":(" : "😞"
}

output = ""
for word in words:
    output += mp.get(word, word) + " "
print(output)