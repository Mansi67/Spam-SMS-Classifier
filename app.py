import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
import contractions
from nltk.stem import WordNetLemmatizer
lemma= WordNetLemmatizer()



def transform_text(text):
    text = contractions.fix(text)
    text = text.lower()

    commonSMS = {
        "Ain’t": "Am not",
        "Wanna": "Want to",
        "Whatcha": "What have you",
        "Kinda": "Kind of",
        "Sorta": "Sort of",
        "Outta": "Out of",
        "Alotta": "A lot of",
        "Lotsa": "Lots of",
        "Mucha": "Much of",
        "Cuppa": "Cup of",
        "Dunno": "Don’t know",
        "Lemme": "Let me",
        "Gimme": "Give me",
        "Tell’em": "Tell them",
        "Imma": "I am going to",
        "Gonna": "Going to",
        "Needa": "Need to",
        "Oughta": "Ought to",
        "Hafta": "Have to",
        "Hasta": "Has to",
        "Usta": "Used to",
        "Supposta": "Supposed to",
        "Gotta": "Got to",
        "Cmon": "Come on",
        "Ya": "You",
        "Shoulda": "Should have",
        "Shouldna": "Should not have",
        "Wouldna": "Would not have",
        "She’da": "She would have",
        "Coulda": "Could have",
        "Woulda": "Would have",
        "Mighta": "Might have",
        "Mightna": "Might not have",
        "Musta": "Must have",
        "Mussna": "Must not have",
        "Dontcha": "Do not you",
        "Wontcha": "Would not you",
        "Whatcha": "What are you",
        "Betcha": "Bet you",
        "Gotcha": "Got you",
        "D’you": "Do you",
        "Didntcha": "Did not you",
        "Dija": "Did you",
        "S’more": "Some more",
        "Layder": "Later",
        "R": "are",
        "N": "and",
        "D": 'the',
        "BRB": "Be right back",
        "IKR": "I know, right",
        "ILY": "I love you",
        "LMFAO": "Laughing my freaking ass off",
        "NVM": "Never mind",
        "OFC": "Of course",
        "ROFL": "Rolling on the floor laughing",
        "SMH": "Shaking my head",
        "STFU": "Shut the fuck up",
        "YOLO": "You only live once",
        "MMB": "Message me back",
        "YNT": "Why not",
        "BW": "Between",
        "TC": "Take care",
        "MU": "Miss you",
        "S2R": "Send to receive",
        "NVM": "Never mind",
        "CTN": "Can’t talk now",
        "B4": "Before",
        "FTW": "For the win",
        "HW": "Homework",
        "W8": "Wait",
        "PC": "Personal computer",
        "ITT": "In this thread",
        "RBTL": "Read between the lines",
        "ETA": "Estimated time of arrival",
        "XOXO": "Hugs and kisses",
        "AFK": "Away from keyboard",
        "BuBye": "Bye Bye",
        "DIY": "Do it yourself",
        "MW": "On my way",
        "SD": "Sweet dreams",
        "YW": "You are welcome",
        "RL": "Real life",
        "SRY": "Sorry",
        "DIKU": "Do I know you",
        "IDGI": "I do not get it",
        "IDC": "I do not care",
        "IDK": "I do not know",
        "CFY": "Calling for you",
        "AAMOF": "As a matter of fact",
        "TYT": "Take your time",
        "TY": "Thank you",
        "GG": "Good game",
        "IRL": "In real life",
        "GJ": "Good job",
        "POV": "Point of view",
        "R8": "Right",
        "BTW": "By the way",
        "SU": "Shut up",
        "NC": "No comment",
        "SEC": "Second",
        "IMO": "In my opinion",
        "JK": "Just kidding",
        "KK": "Okay cool",
        "PPL": "People",
        "GTG": "Got to go",
        "NP": "No problem",
        "ROFL": "Rolling on the floor laughing",
        "RIP": "Rest in peace",
        "SMH": "Shaking my head",
        "PLZ": "Please",
        "RT": "Real time",
        "CYL": "Call you later",
        "GM": "Good morning",
        "GR8": "Great",
        "YOLO": "You only live once",
        "GN": "Goodnight",
        "WD": "Well done",
        "TTYS": "Talk to you soon",
        "BD": "Big deal",
        "GL": "Good luck",
        "L8R": "Later",
        "TTYL": "Talk to you later",
        "TMI": "Too much information",
        "IM": "Instant message",
        "ASIC": "As soon as I can",
        "TCO": "Taken care of",
        "BBIAB": "Be back in a bit",
        "B4N": "Bye for Now",
        "HU": "Hug you",
        "QT": "Cutie",
        "MSG": "Message",
        "LOL": "laugh out loud",
        "ZZZ": "Sleeping",
        "IC": "I see",
        "JJ": "Just joking",
        "F2F": "Face to face",
        "BRB": "Be Right Back",
        "CTN": "Can not talk now",
        "TTYN": "Talk to you never",
        "BFF": "Best Friends Forever",
        "GBTW": "Get back to work",
        "LMAO": "laughing my ass off",
        "BC": "Because",
        "PLS": "Please",
        "NOOB": "Newbie",
        "WTF": "What the fuck",
        "CU": "See you",
        "FAB": "Fabulous",
        "THX": "Thanks",
        "CUL": "See you later",
        "COZ": "Because",
        "CUZ": "Because",
        "CAUSE": "Because",
        "CYA": "See You",
        "Y": "Why",
        "TXT": "Text",
        "KU": "Kiss you",
        "FYI": "For your information",
        "OOO": "Out of office",
        "FAQ": "Frequently asked questions",
        "LU": "Love you",
        "AKA": "Also known as",
        "THO": "Though",
        "BAU": "Business as usual",
        "HBU": "How about you",
        "LMAO": "Laughing my ass off",
        "AFAIK": "As far as I know",
        "BA3": "Battery",
        "GMV": "Got my vote",
        "RT": "Retweet",
        "IMHO": "In my humble opinion",
        "HTH": "Here to help",
        "BF": "Boyfriend",
        "PC": "Personal computer",
        "L8": "Late",
        "ASAP": "As soon as possible",
        "GONNA": "Going to",
        "GUNNA": "Going to",
        "OMG": "Oh my God",
        "LAM": "Leave a message",
        "NTN": "No thanks needed",
        "SS": "So sorry",
        "M8": "Mate",
        "2MORO": "Tomorrow",
        "LNG": "Long",
        "pic": "picture",
        "OMG": "Oh my god",
        "GAL": "Girl",
        "DND": "Do not disturb",
        "10Q": "Thank you",
        "2B": "To be",
        "4EVA": "Forever",
        "2MOR": "Tomorrow",
        "YT": "YouTube",
        "utube": "Youtube",
        "der": "there",
        "wrk": "work",
        "tv": "television",
        "lol": "Laugh out loud",
        "4got": "Forgot",
        "yr": "year",
        "hr": "hour",
        "b4": "before",
        "bout": "about",
        "c": "see",

    }
    new_dict = dict((k.lower(), v.lower()) for k, v in commonSMS.items())
    text_decontracted = []

    for word in text.split():
        if word in new_dict:
            word = new_dict[word]
        text_decontracted.append(word)

    text = ' '.join(text_decontracted)

    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(lemma.lemmatize(i, pos='v'))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
