import re, os
import numpy as np
from numpy import *
import pandas as pd
from pandas import DataFrame, Series
from matplotlib.pyplot import *

########### GLOBALS  ###############
####################################
## NAME
## ROLL_NO
## COLLEGE
## BRANCH
####################################
NAME = ''
ROLL_NO = ''
COLLEGE = ''
BRANCH = ''
cur_sem = 0
sem = []

def start_it() :
	global NAME 
	global ROLL_NO 
	global COLLEGE 
	global BRANCH 
	global cur_sem
	global sem 
	cur_sem = 0
	sem = []
	fii = open('/home/vetron/desktop/myres.txt','r')
	lis = []
	for line in fii :
		lis.append(line)
	lis = lis[9:]
	tlis = []
	for item in lis :
		if len(item) == 3 and item[0] == ' ' :
			cur_sem += 1
			sem.append(list(tlis))
			tlis = []
			continue
		tlis.append(item)

	ROLL_NO = re.sub('Enrollment Number  ','',sem[0][1])#re.findall(r'\d+',sem[1][1])
	NAME = re.sub('Name ','',sem[0][2])#re.findall(r'[A-Z][A-Z].* .*[A-Z]',sem[0][2])
	COLLEGE = re.sub('College','',sem[0][3])#re.findall(r'[A-Z][A-Z].*',sem[0][3])
	BRANCH = re.sub('Stream ','',sem[0][4])
	ROLL_NO = ROLL_NO.split('\n')[0]
	NAME = NAME.split('\n')[0]
	COLLEGE = COLLEGE.split('\n')[0]
	BRANCH = BRANCH.split('\n')[0]
	#print ('NAME : '+NAME+'\nENROLLMENT NO : '+ROLL_NO+'\nBRANCH : '+BRANCH+'\nCOLLEGE : '+COLLEGE)

SubjectID = []
SubjectCode = []
SubjectName = []
InternalMarks = []
ExternalMarks = []
TotalMarks = []
CreditsSecured = []

def do():
	global NAME 
	global ROLL_NO 
	global COLLEGE 
	global BRANCH 
	global cur_sem 
	global sem 
	global SubjectID 
	global SubjectCode 
	global SubjectName 
	global InternalMarks 
	global ExternalMarks 
	global TotalMarks 
	global CreditsSecured 
	df = pd.DataFrame()
	#superdf = pd.DataFrame()
	tot_sem = cur_sem ### 0 indexed based
	cur_sem = 0
	
	while cur_sem < tot_sem :
		tot_subjects = (len(sem[cur_sem])-12+1-4)/7
		
		i = 0 
		line = 12  ### data always starts from line 12
		while i < tot_subjects :
				SubjectID.append(sem[cur_sem][line].split('\n')[0])
				SubjectCode.append(sem[cur_sem][line+1].split('\n')[0])
				SubjectName.append(sem[cur_sem][line+2].split('\n')[0].split(' ',1)[1])
				InternalMarks.append(sem[cur_sem][line+3].split('\n')[0])
				ExternalMarks.append(sem[cur_sem][line+4].split('\n')[0])
				TotalMarks.append(sem[cur_sem][line+5].split('\n')[0].split('*')[0])
				CreditsSecured.append(sem[cur_sem][line+6].split('\n')[0])
				i += 1
				line += 7
		df['SUBJECT_ID'] = Series(SubjectID).astype(float)
		df['SUBJECT_CODE'] = Series(SubjectCode)
		df['SUBJECT_NAME'] = Series(SubjectName)
		df['INTERNAL_MARKS'] = Series(InternalMarks)
		df['EXTERNAL_MARKS'] = Series(ExternalMarks)
		df['TOTAL_MARKS'] = Series(TotalMarks)
		df['CREDITS_SECURED'] = Series(CreditsSecured)
		df = df.dropna()
		df.reset_index()
		ROLL_NO = ROLL_NO.split('\n')[0]
		file_dir = '/home/vetron/desktop/python/bvp_res/'+BRANCH+'/'+ROLL_NO
		#print file_dir
		#raw_input()
		if not os.path.exists(file_dir) :
			os.makedirs(file_dir)
		df.to_csv(file_dir+'/semester'+`cur_sem+1`+'.csv',sep=' ')
		file_name = file_dir+'/semester'+`cur_sem+1`+'.csv'
		tlis = []
		fii = open(file_name,'r+').readlines()
		temp_len = len(fii)
		for num in range(temp_len) :
			fii[num] = fii[num].split(' ',1)[1]
			out = open(file_name,'w')
			out.writelines(fii)
			out.close()
		SubjectID = []
		SubjectCode = []
		SubjectName = []
		InternalMarks = []
		ExternalMarks = []
		TotalMarks = []
		CreditsSecured = []
		cur_sem += 1
def main():
	print 'Starting ....'
	start_it()
	print 'Initialized.\n\nMaking Data Structured....\n'
	do()
	print 'DONE..!!'

if __name__=='__main__':
	main()
