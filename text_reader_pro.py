import pyttsx3

# voice setup
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[3].id)

# speaking function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# format text
def comaMaker(str):
    count = 0
    new_str = ""
    # adding double spaces
    for word in str:
        # if count == 3:
        #     word += "."
        #     count = 0
        if word == " ":
            word += " "
            # count += 1
        new_str += word

    # main work
    nxt_str = ""
    for word in new_str:
        if count == 5:
            word += word.replace(" ", ". ")
            count = 0
        if word == " ":
            count += 1
        nxt_str += word
    # print(nxtStr)
    nxt_str = nxt_str.replace("  ", " ")
    nxt_str = nxt_str.replace(" .", ".")
    # print(nxt_str)
    str = ""
    return nxt_str

# ----------------------------------------------------------------------------------------------------------------------
print("Please. Enter the name of file ")
speak("Please. Enter the name of file ")
fin = input("--> ")
fout_txt = open('text_file.txt', 'w', encoding="utf-8")
str_txt = ""
try:
    with open(fin + ".txt") as f:
        for line in f:
            str_txt += line
    str_txt = str_txt.replace('\n', ' ')
    single_spaces = ' '.join(str_txt.split())
    single_spaces = single_spaces.replace('.', '.\n')
    single_spaces = comaMaker(single_spaces)
    fout_txt.write(single_spaces)
    fout_txt.close()
except SyntaxError:
    print("Something went wrong..")
    speak("Something went wrong..")

# ---------------------------------------------------------------------------------------------------------------------
# speaking the book
print("For better Experience. I format your doc According to my taste.")
speak("For better Experience. I format your doc According to my taste.")
try:
    print("Lets start listening...")
    speak("Lets start listening...")
    with open('text_file.txt', 'r', encoding='UTF-8') as t:
        for line in t:
            print(line, end='')
            speak(line)
    print("..\n\nBook or File is completed...\n Hopefully you enjoyed it. Bye Bye")
    speak("..\n\nBook or File is completed...\n Hopefully you enjoyed it. Bye Bye")
except:
    print("Something went wrong..")
    print("Sometime the text format inside text file is different.")
