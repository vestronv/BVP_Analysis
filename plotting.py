import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = '/home/vetron/desktop/python/bvp_res/Computer Science & Engineering(U)/01751202712/semester'

#~ IM = """
#~ INTERNAL_MARKS
#~ """
#~ EM = """
#~ EXTERNAL_MARKS
#~ """
#~ TM = """
#~ TOTAL_MARKS
#~ """
#~ CD = """
#~ CREDITS
#~ """
#~ SN = """
#~ SUBJECT_NAME
#~ """

sem1 = pd.read_csv(path+'1.csv',sep=' ')
sem2 = pd.read_csv(path+'2.csv',sep=' ')
sem3 = pd.read_csv(path+'3.csv',sep=' ')
sem4 = pd.read_csv(path+'4.csv',sep=' ')
sem5 = pd.read_csv(path+'5.csv',sep=' ')

plt.plot(sem1.INTERNAL_MARKS,'r',sem2.INTERNAL_MARKS,'b',sem3.INTERNAL_MARKS,'g',sem4.INTERNAL_MARKS,'y',sem5.INTERNAL_MARKS,'k')
plt.hist(sem1.INTERNAL_MARKS)#,sem5.INTERNAL_MARKS)
#plt.plot(sem1.EXTERNAL_MARKS,'r',sem2.EXTERNAL_MARKS,'b',sem3.EXTERNAL_MARKS,'g',sem4.EXTERNAL_MARKS,'y',sem5.EXTERNAL_MARKS,'k')
plt.show()

print lis=[(sem1.TOTAL_MARKS.mean(),sem2.TOTAL_MARKS.mean(),sem3.TOTAL_MARKS.mean(),sem4.TOTAL_MARKS.mean(),sem5.TOTAL_MARKS.mean())]

