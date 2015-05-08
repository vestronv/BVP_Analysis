import urllib, urllib2, cookielib, mechanize, re, os
#from bs4 import BeautifulSoup as bs
from import_file import import_file as impf
crazy1 = impf('/home/vetron/desktop/python/bvp_res/result_bvp_cont.py')

#ROLL = ''
def con_n_save_data(roll):
	#username = 'myuser'
	#password = 'mypassword'
	print 'Connecting ... '
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	login_data = urllib.urlencode({'Roll_No' : (roll)})
	opener.open('http://www.ipuresult.com/index.php', login_data)

	stu_marks_raw = opener.open('http://www.ipuresult.com/student_marks.php').read()
	all_marks_raw = opener.open('http://www.ipuresult.com/all.php').read()
	overview_raw = opener.open('http://www.ipuresult.com/overview.php').read()
	print 'Connected and loaded data...\nProcessing.....\n'
	print 'Saving Data .....'
	all_marks_raw = all_marks_raw[987:]
	start = False
	end = False
	lis = []
	mystr = ''
	for ch in all_marks_raw :
		if ch == '<' :
			start = False
			if len(mystr) > 0 :
				mystr = re.sub(':&nbsp',' ',mystr)
				mystr = re.sub('&nbsp','',mystr)
				lis.append(mystr)
				mystr = ''
		if ch == '>' :
			start = True
		if start == True and ch != '>' and ch != '\n':
			mystr+=ch
	fi = open('/home/vetron/desktop/myres.txt','w')
	for item in lis :
		fi.write(item)
		fi.write('\n')
	fi.write('  \n')
	fi.close()

if __name__=='__main__' :
	fi = open('/home/vetron/desktop/python/bvp_res/ROLL.txt','r').readlines()
	global ROLL
	for line in fi: 
		ROLL=line.split('\n')[0]+'51202712'
		con_n_save_data(ROLL)
		print 'Roll ',ROLL,' over.\n\n'
		print '\n'
		crazy1.ROLL_NO=ROLL
		crazy1.main()
		os.system('clear')
	print 'DONE'
