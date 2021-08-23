import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import pass1



engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def greet():
	hour = int(datetime.datetime.now().hour)
	
	if hour>=0 and hour<12:
		speak("good morning Mam")

	elif hour>=12 and hour<18:
		speak("good afternoon Mam")
	
	else:
		speak("Good Evening Mam")

	speak("I am jarvis Mam, Tell me how can i help you?")

def takeCommand():
	
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		
	try:
		print("Recognizing...")
		query = r.recognize_google(audio,language='en-in')
		print(f"User said; {query}\n")

	except Exception as e:
		print(e)
		print("Say That Again Please...")
		return "None"

	return query

def sendEmail(to,content):
	e = pass1.getEmail()
	p = pass1.getPass()

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login(e,p)
	server.sendmail(e,to,content)
	server.close()


if __name__ == "__main__":
	greet()
	while True:
		query = takeCommand().lower()
		
		
		if 'according to wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace('according to wikipedia','')
			results = wikipedia.summary(query,sentences=2)
			speak("According to wikipedia")
			print(results)
			speak(results)

	  	

		elif 'open youtube' in query:
			speak('opening youtube..')
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak('opening google..')
			webbrowser.open("google.com")
		
		elif 'github' in query:
			speak('opening github')
			webbrowser.open("github.com")

		elif 'facebook' in query:
			speak('opening facebook')
			webbrowser.open("facebook.com")

		elif 'instagram' in query:
			speak('opening instagram')
			webbrowser.open("instagram.com")
		

	

		elif 'according to google' in query:
			speak('opening google')
			query = query.replace('according to google','')
			webbrowser.open('http://google.com/#q='+query,new=2)

		elif 'what is the time now' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print(strTime)
			speak(f"Mam,the time is {strTime}")

		elif 'play music' in query:
			music_dir = 'C:\\Users\\prava\\OneDrive\\Documents\\Desktop\\songs'
			songs = os.listdir(music_dir)
			n = len(songs)
			index = random.randint(1,n)
			os.startfile(os.path.join(music_dir,songs[0]))

		elif 'send mail' in query:
			try:
				speak("What should i say?")
				content=takeCommand()
				to = "pravallika.work@gmail.com"
				sendEmail(to,content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry Mam,I am not able to send this email")

                  