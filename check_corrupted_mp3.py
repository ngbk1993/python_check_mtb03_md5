import os 
import hashlib
import sys

#Magic Number to compare
FileHashDict={
"01 点.mp3" : "cb93a900a5a810dea8ddbb6fe3bd0af8",
"02 心圆满.mp3" : "4b4bf5ae27b3b107240aac3d8314a82d",
"03 我不怕.mp3" : "02cdd8ce9119dbef775a40130dead479",
"04 奔跑.mp3" : "8a8664f1ac388d859a0fb7342350d6b4",
"05 为生活点like.mp3" : "3b7c8355a261ad66b63c9b7c343f1b31",
"06 Together We Build a Home.mp3" : "8b658dfbf84cf63cae6438cf5f5ebc9e",
"07 四重恩.mp3" : "01996c2a83d169d8172209bd966fdddb",
"08 约定陪你.mp3" : "b5720fba87a952e92f2469aeb8075aac",
"09 下一季，再来.mp3" : "4b48d08e87772f666082fdde55bb3743",
"10 与愿起飞.mp3" : "2145d22e0988a46045fa4dd3e2ab721b",
"MTB03_歌词.pdf" : "2111b530007c63fbb87b6475b6a1dbc2"
}

#Magic Number 2 to compare
FileHashDict2={
"01 点.mp3" : "cb93a900a5a810dea8ddbb6fe3bd0af8",
"02 心圆满.mp3" : "4b4bf5ae27b3b107240aac3d8314a82d",
"03 我不怕.mp3" : "815aff6ec566ea51b260a5a112d24ea6",
"04 奔跑.mp3" : "8a8664f1ac388d859a0fb7342350d6b4",
"05 为生活点like.mp3" : "3b7c8355a261ad66b63c9b7c343f1b31",
"06 Together We Build a Home.mp3" : "ac13de109574f5ad2a339fa722a163ce",
"07 四重恩.mp3" : "01996c2a83d169d8172209bd966fdddb",
"08 约定陪你.mp3" : "b5720fba87a952e92f2469aeb8075aac",
"09 下一季，再来.mp3" : "4b48d08e87772f666082fdde55bb3743",
"10 与愿起飞.mp3" : "a40a87d4389d32c9c805aa932da5c2cc",
"MTB03_歌词.pdf" : "2111b530007c63fbb87b6475b6a1dbc2"
}

def getFileMd5(file_name):
     # Open,close, read file and calculate MD5 on its contents     
     with open(file_name, 'rb') as file_to_check:
         # read contents of the file
         data = file_to_check.read()    
         # pipe contents of the file through
         md5_returned = hashlib.md5(data).hexdigest()     
         return md5_returned
    
def scan_file_md5(theDrive):
    levelcount = 0
    filecount = 0
    Failure = 0
    
    for path,dirs,files in os.walk(theDrive):
        if (levelcount >= 1):
            #Check only the root folder
            break
        for filename in files:
            # build the source path
            src = os.path.join(path,filename)
            if filename in FileHashDict.keys():
                # checking if it is a file
                if  (os.path.isfile(src)):
                    print("Processing %s" % src)
                    #print(getFileMd5(src))
                    if ((getFileMd5(src) != FileHashDict[filename]) and (getFileMd5(src) != FileHashDict2[filename])):
                        print("Error: File Corrupted %s" % src)
                        Failure += 1
                        
                    print("")
                    print("")
                    
                    filecount += 1
        
        print ("%d files checked %d files failed" % (filecount, Failure))
        levelcount += 1
        filecount=0

scan_file_md5(sys.argv[1])