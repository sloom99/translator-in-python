#to replace vowels in a phrase with g

def translation(phrase):
    translate = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translate = translate + "G"
            else:
                translate = translate + "g"
        else:
            translate = translate + letter
    return translate

print(translation(input("Enter your phrase: ")))
