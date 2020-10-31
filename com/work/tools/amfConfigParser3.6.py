
from xml.dom.minidom import parse
import xml.dom.minidom

###########################PreConfig######################################
GitRepoPath ="C:\\DevelopmentFolder\\GitRepository\\"
TIBCO_HOME = "C:\\ProgramData\\TIBCO_HOME\\"

###########################Functions######################################
def getQueueNameList(fileName, Items):
	try:
		DOMTree = xml.dom.minidom.parse(fileName)
	except:
		print ("Failed to find the file path "+fileName+".\n")
		return
	amfsystem = DOMTree.documentElement
	# Get all the movies in the collection
	receiver_msgdestinations = amfsystem.getElementsByTagName("receiver")[0].getElementsByTagName("msg-destinations")[0].getElementsByTagName("msg-destination")
	sender_msgdestinations = amfsystem.getElementsByTagName("sender")[0].getElementsByTagName("msg-destinations")[0].getElementsByTagName("msg-destination")

	# Print detail of each movie.

	for msgdestination in receiver_msgdestinations:
	  # print msgdestination.getElementsByTagName("dest-name")[0].childNodes[0].data
	  #  print msgdestination.getElementsByTagName("queue")[0].getElementsByTagName("dest-exception-queue-name")[0].childNodes[0].data
	   Items.add(msgdestination.getElementsByTagName("dest-name")[0].childNodes[0].data)
	   Items.add(msgdestination.getElementsByTagName("queue")[0].getElementsByTagName("dest-exception-queue-name")[0].childNodes[0].data)

	#print "*****Sender QUEUE*******"
	for msgdestination in sender_msgdestinations:
	   # print msgdestination.getElementsByTagName("dest-name")[0].childNodes[0].data
		if msgdestination.getElementsByTagName("isQueue")[0].childNodes[0].data =="true":
			#print msgdestination.getElementsByTagName("dest-name")[0].childNodes[0].data
			Items.add(msgdestination.getElementsByTagName("dest-name")[0].childNodes[0].data)


def getTopicNameList(fileName, Items):
	DOMTree = xml.dom.minidom.parse(fileName)
	amfsystem = DOMTree.documentElement
	# Get all the movies in the collection
	sender_msgdestinations = amfsystem.getElementsByTagName("sender")[0].getElementsByTagName("msg-destinations")[0].getElementsByTagName("msg-destination")
	# Print detail of each movie.
	#print "*****Sender TOPIC*******"
	for msgdestination in sender_msgdestinations:
		if msgdestination.getElementsByTagName("isQueue")[0].childNodes[0].data =="false":
			Items.add(msgdestination.getElementsByTagName("dest-name")[0].childNodes[0].data)

def updateTibcoHomeConfig(filePath, items, type):
	file = open(filePath,"r+")
	lines = file.readlines()
	endNum = 0
	foundInd = False
	for line in lines:
		if (type == "queue" and line.rstrip().lstrip() =="queue.sample") or (type == "topic" and line.rstrip().lstrip()=="topic.sample"):
			print ("Found "+line+"line number = "+str(endNum))
			foundInd = True
			break
		endNum = endNum+1
	if(foundInd):
		file.seek(0)
		file.truncate()
		file.writelines(lines[0:endNum+1])
		file.write("\n\n\n")
		for name in items:
			file.write(name+"\n")
		print ("Update "+filePath+" successfully\n")
	else:
		if (type == "topic"):
			print ("Failed to update "+filePath+".\nCannot find 'topic.sample' in the file\n")
		if (type == "queue"):
			print ("Failed to update "+filePath+".\nCannot find 'queue.sample' in the file\n")
	file.close()

#***********Default Values***************************
CDM_configFile = "iris4_cdm\\WLS_DOM_CDM\\war_file\\target\\m2e-wtp\\web-resources\\WEB-INF\\classes\\amfConfig.xml"
ACM_configFile = "iris4_acm\\WLS_DOM_ACM\\war_file\\target\\classes\\amfConfig.xml"
ACMI_configFile = "iris4_acm\\WLS_DOM_ACMI\\war_file\\target\\m2e-wtp\\web-resources\\WEB-INF\\classes\\amfConfig.xml"
MainProcessor_configFile = "\\iris4_acm\\WLS_DOM_ACM\\war_MainProcessor\\src\\main\\resources\\amfConfig.xml"

queueConfFile="tibco\\cfgmgmt\\ems\\data\\queues.conf"
topicConfFile="tibco\\cfgmgmt\\ems\\data\\topics.conf"

#***************Main Function********************
#print "*****QUEUE*******"
CDM_amfConfigPath = GitRepoPath+CDM_configFile
ACM_amfConfigPath = GitRepoPath+ACM_configFile
ACMI_amfConfigPath = GitRepoPath+ACMI_configFile
MainProcessor_amfConfigPath = GitRepoPath+MainProcessor_configFile

queueConfPath = TIBCO_HOME + queueConfFile
topicConfPath = TIBCO_HOME + topicConfFile

print ("*********Config Values*******")
print ("CDM amfconfig file path:\n"+CDM_amfConfigPath)
print ("\nACM amfconfig file path:\n"+ACM_amfConfigPath)
print ("\nACMI amfconfig file path:\n"+ACMI_amfConfigPath)
print ("\nMainProcessor amfconfig file path:\n"+MainProcessor_configFile)
print ("\nTIBCO_HOME queue.config filepath:\n"+queueConfPath)
print ("\nTIBCO_HOME topic.config filepath:\n"+topicConfPath)

print ("\n")
queitems = set()
getQueueNameList(ACM_amfConfigPath,queitems)
getQueueNameList(ACMI_amfConfigPath,queitems)
getQueueNameList(CDM_amfConfigPath,queitems)
getQueueNameList(MainProcessor_amfConfigPath,queitems)
queitems = sorted(queitems)

#print "*****TOPIC*******"
tpcitems = set()
getTopicNameList(ACM_amfConfigPath,tpcitems)
getTopicNameList(ACMI_amfConfigPath,tpcitems)
getTopicNameList(CDM_amfConfigPath, tpcitems)
getTopicNameList(MainProcessor_amfConfigPath, tpcitems)
tpcitems = sorted(tpcitems)


print ("************Program Start***********")
#Options
while(True):
	option = input("Options:\n1. Print Queue and Topic names from git repository\n2. Update the queues.conf and topics.conf in TIBCO_HOME\n3. Quit\n\nPlease Choose your option:")
	if option == "1":
		print ("*****QUEUE*******")
		for name in queitems:
			print (name)
		print ("\n")
		print ("*****TOPIC*******")
		for name in tpcitems:
			print (name)
		print ("\n\n\n")
	elif option == "2":
		print ("Option2")
		updateTibcoHomeConfig(queueConfPath,queitems, "queue")
		updateTibcoHomeConfig(topicConfPath,tpcitems, "topic")
	elif option =="3":
		print ("Bye Bye!!\n\n")
		quit()
	else:
		print ("wrong input!!\n\n")
