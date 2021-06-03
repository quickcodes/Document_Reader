import pyttsx3

# voice setup
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[3].id)

# Speaking function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Format text
def comaMaker(str):
    count = 0
    new_str = ""
    # Adding double spaces
    for word in str:
        if word == " ":
            word += " "
        new_str += word

    # Main work
    nxt_str = ""
    for word in new_str:
        if count == 5:
            word += word.replace(" ", ". ")
            count = 0
        if word == " ":
            count += 1
        nxt_str += word
    nxt_str = nxt_str.replace("  ", " ")
    nxt_str = nxt_str.replace(" .", ".")
    str = ""
    return nxt_str

# ----------------------------------------------------------------------------------------------------------------------
# Taking input and format file
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
# Speaking the Document
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
