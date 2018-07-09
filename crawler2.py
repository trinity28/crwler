import urllib,re
from bs4 import BeautifulSoup
import csv


#proxies = {'http': 'http://ipg_2015048:apple28@192.168.1.107:3128'}
urls="http://www.mapsofindia.com/states/"
htmlfile=urllib.urlopen(urls,proxies=proxies)
htmltext=htmlfile.read()
soup = BeautifulSoup(htmltext, 'html.parser')
l=[]
i=1
productDivs = soup.find('table',attrs={"class" : "tableizer-table"})

j=1
for s in productDivs.findAll('tr'):
	
	for link in s.findAll('td'):
	    
	    if j<59 and (i%12==1 or (i%6==0 and (i/6)%2!=0) ):
	    	l.append(link.text)
	    	j=j+1
	    i+=1

l2=[['Country','States','City']]

for i in range(0,len(l),2):
	l1=[]
	l1.append('India')
	l1.append(l[i])
	s1=l[i+1].split(",") 
	l1.append(s1[0])
	l2.append(l1)

	l1=[]
	l1.append('India')
	l1.append(l[i])
	if len(s1)>1:
		l1.append(s1[1])
		l2.append(l1)



with open('state.csv', 'w') as myfile:
	a=csv.writer(myfile,delimiter=',')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for x in l2:
		wr.writerow(x)
    

state = raw_input('Enter state to find cities\n')

#read csv, and split on "," the line
def State(state):
	csv_file = csv.reader(open('state.csv', "rb"), delimiter=",")
	#loop through csv list
	for row in csv_file:
	    
	    if state.title() == row[1]:
	         print row[2],
State(state)
