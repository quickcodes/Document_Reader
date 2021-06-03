import pyttsx3
import PyPDF2

# voice setup
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[3].id)


# speaking function
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

# ----------------------------------------------------------------------------
print("Which type of file you have to listen..?")
speak("Which type of file you have to listen..?")
print("Enter 1 for text and 2 for pdf")
speak("Enter 1 for text and 2 for pdf")
inp = input("--> ")
if '1' in inp:
    print("Enter the name of file ")
    speak("Enter the name of file ")
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
        fout_txt.write(single_spaces)
        fout_txt.close()
    except SyntaxError:
        print("Something went wrong..")
        speak("Something went wrong..")
elif '2' in inp:
    print("Enter the name of PDF file. ")
    print("Make sure your pdf have proper text in pdf..")
    print("pdf files are not working with cmd")
    speak("Enter the name of PDF file. ")
    bk = input("--> ")
    book = open(bk, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(f"Total available pages are {pages}")
    speak("There are to many pages available Here")
    print("Enter the number of page I want to speak ?")
    speak("Enter the number of page I want to speak ?")
    pg = int(input("--> "))
    page = pdfReader.getPage(pg)
    str_pdf = page.extractText()
    # --------------------------
    fout_pdf = open('text_file.txt', 'w', encoding='utf-8')
    try:
        str_pdf = str_pdf.replace('\n', ' ')
        single_spaces = ' '.join(str_pdf.split())
        single_spaces = single_spaces.replace('.', '.\n')
        single_spaces = str(single_spaces)
        single_spaces = comaMaker(single_spaces)
        fout_pdf.write(single_spaces)
        fout_pdf.close()
    except SyntaxError:
        print("Something went wrong..")
        speak("Something went wrong..")

else:
    print("Please Enter a valid input.")
    speak("Please Enter a valid input.")

# ----------------------------------------------------------------------------


# speaking the book
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
