import datetime, gtts, bs4, random, speech_recognition

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    #raise RuntimeError("You need to write this part!")
    (date, time) = datetime.datetime.now().isoformat().split("T")
    (hour, minutes, seconds) = time.split(":")
    if lang=="en":
        text = hour+" hours and "+minutes+" minutes"
    elif lang=="ja":
        text = hour+"�r"+minutes+"�֤Ǥ�"
    elif lang=="zh":
        text = "������"+hour+"��"+"��"
    else:
        text="I'm sorry, I don't know that language"
    gtts.gTTS(text,lang=lang).save(filename)
    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    #raise RuntimeError("You need to write this part!")
    filename = 'jokes_%s.txt'%(lang)
    with open(filename) as f:
        jokes = f.readlines()
    joke = random.choice(jokes)
    print(joke.strip())
    gtts.gTTS(joke.strip(), lang=lang).save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    #raise RuntimeError("You need to write this part!")
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    weekday = today.isoweekday()
    if lang=="en":
        weekdays=['','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        months=['','January','February','March','April','May','June','July','August','September','October','November','December']
        text = "%s, %s %d, %d"%(weekdays[weekday],months[month],day,year)
        gtts.gTTS("Today is "+text,lang="en").save(audiofile)
    elif lang=="ja":
        weekdays=' �»�ˮľ������'
        text="%s����,%d��%d��, %d��"%(weekdays[weekday],month,day,year)
        gtts.gTTS("���դ�"+text,lang="ja").save(audiofile)
    elif lang=="zh":
        weekdays=['','��һ','�ܶ�','����','����','����','����','������']
        text='%s, %d��%d��, %d��'%(weekdays[weekday],month,day,year)
        gtts.gTTS("������"+text,lang="zh").save(audiofile)

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    #raise RuntimeError("You need to write this part!")
    if lang=="en":
        keywords = ["what time", "joke", "what day", "I'm sorry, I didn't understand you"]
    elif lang=="ja":
        keywords = ["�Εr","��Մ","����","���ߤޤ��󡢤褯�狼��ޤ���Ǥ���"]
    elif lang=="zh":
        keywords = ["���H","��Ц","ʲô����","�Բ�����û������Ļ�"]
    else:
        speech_package.synthesize("I don't know that language!","en",filename)
        return
    while True:
        print("I heard",text)
        if keywords[0] in text:
            what_time_is_it(lang, filename)
            break
        elif keywords[1] in text:
            tell_me_a_joke(lang, filename)
            break
        elif keywords[2] in text:
            what_day_is_it(lang, filename)
            break
        else:
            print(keywords[3])
            print('I will try again')
