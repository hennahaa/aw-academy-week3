from datetime import datetime
myFile = open('kellonajat.txt', 'a') 
myFile.write('\nKello on: ' + str(datetime.now()))

