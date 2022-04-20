import re
import os
# open the sample file used
file = open("C:/Users/1822569.INDIA/Documents/WIP/WIP_1/project-2/ebooks.txt")
# read the content of the file opened
content = file.readlines()

key=input("You: ")

flag=0
a = []
for i in range(0,len(content)):
 line=content[i].casefold()
 x  = re.search(key.casefold(),line.strip(),re.IGNORECASE)
 if x is not None:
  a.append(line.strip())
  flag=1 
  
#--Operation: search in the directory 
if flag == 1:
 print("\nSystem: Matches found -")
 for i in range(0,len(a)):
     print("\t\t[",i+1,"]",a[i])
 print("\n\t\tEnter book name: ")
 option =input("You: ")
 option=str(option)
 print("\nSystem: Thank you for choosing-\n\t\t\t****",option,"****")
 #init = key[0].upper()
 
 print("\n\t---switching to the pdf file----")
 
 ######################## data file ################
 if option == "Learning SQL by Alan Beaulieu":
     os.system("start \"\" https://drive.google.com/file/d/1Knx-SiNk1dOpn-Dzzv0OsFFVYAtuNkbC/view?usp=sharing")
 
 elif option == "Mastering pandas by Femi Anthony":
     os.system("start \"\" https://drive.google.com/file/d/16Tnq5Y_zzKw5gZzUf5sZYTbIrTTa60ka/view?usp=sharing")
 
 elif option == "MySQL Cookbook by Paul DuBois":
     os.system("start \"\" https://drive.google.com/file/d/1_NpV4duR8OKqZClzsY1TJD1Kp-TeS1j-/view?usp=sharing")
 
 elif option == "Head First SQL by Lynn Beighley":
     os.system("start \"\" https://drive.google.com/file/d/1Q4dK7w8Uy0O9f-Tb8cr-MNvOyDJtFA1i/view?usp=sharing")
 
 elif option == "Programming in Python by Mark Summerfield":
     os.system("start \"\" https://drive.google.com/file/d/1JQGFRoacS-iOtgwzGux0tWYKKDUEljo4/view?usp=sharing")
 
 elif option == "Python ESSENTIAL REFERENCE by David M. Beazley":
     os.system("start \"\" https://drive.google.com/file/d/1iUzIskKl8OsPXm4ZlpxqxM_eK0I_-D97/view?usp=sharing")
 
 elif option == "Python Cookbook by David Beazley and Brian K. Jones":
     os.system("start \"\" https://drive.google.com/file/d/1lPfRtQM-olECDjtxq2Qr2AgxVV3CmynL/view?usp=sharing")
 
 elif option == "Python for Data Analysis by Wes McKinney":	
     os.system("start \"\" https://drive.google.com/file/d/1dHoQNsgf7tUfMarkhk0wllTvgWG2eb-p/view?usp=sharing")
 
 elif option == "Python Programming Examples":	
     os.system("start \"\" https://drive.google.com/file/d/1Mlyja_e67t3Lxz_BF1Y8Hb11eeQfNNh4/view?usp=sharing")
 
 elif option == "R Graphics Cookbook by Winston Chang":	
     os.system("start \"\" https://drive.google.com/file/d/1mAxzSpF4-s10mJsTz1OvgSyyjthMwaW0/view?usp=sharing")
 
 elif option == "R Cookbook by Paul Teetor":	
     os.system("start \"\" https://drive.google.com/file/d/1qBeoZMVYL4Ip6zvWfFDG1MU9aiXhIZQH/view?usp=sharing")
 
 elif option == "R Programming for Data Science by Roger D. Peng":	
     os.system("start \"\" https://drive.google.com/file/d/1xezr91MQ6P1Zwn-tE35DvHoncDghF2LU/view?usp=sharing")
 
 elif option == "R For Dummies- by by Andrie de Vries and Joris Meys":	
     os.system("start \"\" https://drive.google.com/file/d/1PwdXkQVreCYwn9pOS305a99wHq2aei__/view?usp=sharing")
 
 elif option == "Hands-On Programming with R by Garrett Grolemund":	
     os.system("start \"\" https://drive.google.com/file/d/1NzoPf-R4txlv8jrfwchQSOUVUQFOfNf1/view?usp=sharing")
 
 elif option == "Getting Started with RStudio by John Verzani":	
     os.system("start \"\" https://drive.google.com/file/d/16d1wXHk0QnIxiISZsm_3DA5vDNM0XzKg/view?usp=sharing")
 
 elif option == "R programming by Tutorialspoint":
   	 os.system("start \"\" https://drive.google.com/file/d/1wmzLqp6eYQEc-BCOmTHqktcps92xzZpo/view?usp=sharing")
 
 elif option == "SQL: The Complete Reference by James R. Groff and Paul N. Weinberg":	
     os.system("start \"\" https://drive.google.com/file/d/1krwpIs4SskZ6agjpGm1rZfDluIOTsJeP/view?usp=sharing")
 
 
 elif option == "SQL-1 by Tutorialspoint"	:
     os.system("start \"\" https://drive.google.com/file/d/1pjOCr-6j_VlVAqkuxrzP2gOzIS4TitbI/view?usp=sharing")
 
 elif option == "SQL-2 by Tutorialspoint"	:
     os.system("start \"\" https://drive.google.com/file/d/1dmaMHjBu6bILvzmTrBbckJR_hA_H1DOK/view?usp=sharing")
 
 elif option == "Programming Python by Mark Lutz":
     os.system("start \"\" https://drive.google.com/file/d/1_cfibgmt8LUrQQk82oKh2j7B55Niw6hB/view?usp=sharing")

 
 #os.system("start \"\" https://drive.google.com/drive/folders/1WU2aw9_WvGRbx-2k5wv0linWrQPJ4jKn")


else:
 print("\nSystem: please search again")


#a.clear()
#os.system("start \"\" https://en.wikipedia.org/wiki/Seahorse")

