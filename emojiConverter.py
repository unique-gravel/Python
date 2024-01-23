def emojiConverter(message):
    words = message.split(" ")
    mp  = {
        ":)" : "😀",
        ":(" : "😞"
    }
    output = ""
    for word in words:
        output += mp.get(word, word) + " "
    return output

message = input("> ")
result = emojiConverter(message)
print(result)