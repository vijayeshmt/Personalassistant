import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


# To change the voice to female change 0 to 1.


def speak(audio):
	engine.say(audio)
	engine.runAndWait()
	pass


def take_command():
	"""
	It takes microphone input from the user and returns a  string

	:return:
	"""
	r = sr.Recognizer()
	with sr.Microphone() as  source:
		print("Listening...")
		r.pause_threshold = 1.5  # It will wait 1.5 seconds to complete a sentence
		audio = r.listen(source)
		#Do read details
	try:
		print("Recognizing")
		query = r.recognize_google(audio,language='en-in')
		print(f'user said : {query}\n')

	except Exception as e:
		#print(e)
		print("Say that again please")
		return "None"
	return query
def sendEmail(to,content):
	server =smtplib.SMTP('smtp.gmail.com',28)
	# server.connect("smtp.gmail.com",465)
	# server.ehlo()
	server.login('jayeshvijayesh@gmail.com','########')
	server.sendmail('jayeshvijayesh@gmail.com',to,content)
	server.close()
def wish_me():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		speak("Good morning")
	elif hour >= 12 and hour < 18:
		speak("Good afternoon")

	else:
		speak("Good night")
	speak("I am JARVIS how can i  help you")


if __name__ == '__main__':
	wish_me()
	while True:
		query =take_command().lower()
		if 'wikipedia' in query:
			speak("Searching wikipedia")
			query = query.replace('wikipedia','')
			results = wikipedia.summary(query,sentences=2)#To read more increase sentence to decrease sentence decreease sentence
			speak("According to wikipedia")
			#print(results)
			speak(results)
		elif  'open youtube' in  query:
			# webbrowser.Chrome.open_new("youtube.com")
			webbrowser.open("youtube.com")
		elif "open google" in query:
			webbrowser.open("google.com")
		elif "open spotify" in query:
			webbrowser.open("open.spotify.com")


		elif "play music" in query:
			music_dir = "D:\\vijayesh\\music"
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir,songs[1]))

		elif "the time" in query:
			strtime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"The time is {strtime}")
		elif " open pycharm" in query:
			pycharmpath ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021"
			os.startfile(pycharmpath)
		elif "exit" in query:
			exit()
		#elif "open command" in query:
			# filelocation = "path of the particular file like above"
			# os.startfile(filelocation)
		elif " email to vijayesh" or "email to vijesh" in query:
			try:
				speak("What should i say")#error present
				content = take_command()
				to = "jayeshvijayesh@gmail.com"
				sendEmail(to,content)
				speak("Email has been sent")
				exit()
			except Exception as e:
				print(e)
				speak("Sorry,I am not able to send this email")
				exit()
				
