import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
	message=raw_input("Enter your message >> ")
	if message=="quit":
		exit()
	elif message=="bye":
		exit()
	elif message=="bye bye":
		exit()
	elif message=="good bye":
		exit()
	elif message=="see u":
		print "Okay then :)"
		exit()
	elif message=="save":
		kernel.saveBrain("bot_brain.brn")	
	else:
		res= kernel.respond(message)
		print res
		cm='espeak -ven-us+f3 -s155 "'+res+'"'
		os.system(cm)

