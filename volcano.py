
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:

eruptions = pd.io.excel.read_excel('Eruptions.xlsx', header = 1)
volcanoes = pd.io.excel.read_excel('Volcanoes.xlsx', header = 1)
eruptions.head()


# In[230]:

volcanoes.head()


# In[231]:

print eruptions.columns, '\n','\n', volcanoes.columns


# In[232]:

conf_erup = eruptions[eruptions['Eruption Category'] == 'Confirmed Eruption']


# In[233]:

print conf_erup.shape
conf_erup.head()


# In[234]:

conf_erup['Start Year Uncertainty'].fillna(0, inplace = True)
conf_erup['Start Day Uncertainty'].fillna(0, inplace = True)
conf = conf_erup[(conf_erup['Start Year Uncertainty'] == 0) & (conf_erup['Start Day Uncertainty'] == 0)]
print conf.shape
conf.head()


# In[235]:

conf_erup = conf
conf_erup.drop('Start Year Uncertainty', 1, inplace = True)
conf_erup['Start Day Uncertainty'].unique()


# In[236]:

conf_erup.drop('Start Day Uncertainty', 1, inplace = True)
conf_erup.head()


# In[237]:

#plt.figure(figsize=(6,20))
conf_erup.hist(['Start Year'], bins = 100, log = True, figsize = (20,6))
plt.xlim([-10000, 2100])
plt.show()

conf_erup.hist(['Start Month'], bins = 100, figsize = (20,6))


# In[238]:

conf_erup = conf_erup[conf_erup['Start Month']!=0]
conf_erup = conf_erup[conf_erup['Start Day']!=0]
conf_erup.shape


# In[239]:

conf_erup.hist(['Start Month'], bins = 100, figsize = (20,6))
plt.ylim([250,350])
plt.hlines(y = 302, xmin = 0, xmax= 12)
plt.show()


# In[240]:

avg = len(conf_erup['Volcano Number'])/12
avg


# In[241]:

conf_erup['Start Month'].unique()


# In[242]:

conf_erup['Start Month'].fillna(0, inplace = True)
conf_erup['Start Day'].fillna(0, inplace = True)
conf_erup = conf_erup[(conf_erup['Start Month'] != 0) & (conf_erup['Start Day'] != 0)]

average = conf_erup.shape[0]/12.

conf_erup.hist(['Start Month'], bins = 100, figsize = (20,6))
plt.ylim([250,350])
plt.hlines(y = average, xmin = 0, xmax= 12)
plt.show()


# In[243]:

month = [0]*12
for i in xrange(12):
    month[i] = (len(conf_erup[conf_erup['Start Month'] == i+1]['Start Month'])-average)/average
plt.bar([1,2,3,4,5,6,7,8,9,10,11,12],month )



# In[244]:

conf_erup = conf_erup[conf_erup['Evidence Method (dating)']=='Historical Observations']
average = conf_erup.shape[0]/12.
conf_erup.hist(['Start Month'], bins = 100, figsize = (20,6))
#plt.ylim([250,350])
plt.hlines(y = average, xmin = 0, xmax= 12)
plt.show()
print conf_erup.shape

for i in xrange(12):
    month[i] = (len(conf_erup[conf_erup['Start Month'] == i+1]['Start Month'])-average)
plt.bar([1,2,3,4,5,6,7,8,9,10,11,12],month )
plt.show()


# In[245]:

conf_erup['VEI'].unique()


# In[246]:

conf_erup['VEI'].fillna('NA', inplace = True)
conf = conf_erup[conf_erup['VEI'] != 'NA']
conf_erup = conf
print conf_erup.shape


# In[247]:

average = conf_erup.shape[0]/12.
conf_erup.hist(['Start Month'], bins = 100, figsize = (20,6))
plt.ylim([250, 350])
plt.hlines(y = average, xmin = 0, xmax= 12)
plt.show()

for i in xrange(12):
    month[i] = (len(conf_erup[conf_erup['Start Month'] == i+1]['Start Month'])-average)
plt.bar([1,2,3,4,5,6,7,8,9,10,11,12],month )
plt.show()


# In[248]:

conf_erup2002 = conf_erup[(conf_erup['Start Year'] <= 2014) & (conf_erup['Start Year']>1700)]
print conf_erup2002.shape
average = conf_erup2002.shape[0]/12.
conf_erup2002.hist(['Start Month'], bins = 100, figsize = (20,6))
plt.ylim([150, 300])
plt.hlines(y = average, xmin = 0, xmax= 12)
plt.show()

for i in xrange(12):
    month[i] = (len(conf_erup2002[conf_erup2002['Start Month'] == i+1]['Start Month'])-average)
plt.bar([1,2,3,4,5,6,7,8,9,10,11,12],month )
plt.show()


# In[249]:

conf_erup2014 = conf_erup[conf_erup['Start Year'] > 2000]
print conf_erup2014.shape
average = conf_erup2014.shape[0]/12.
conf_erup2014.hist(['Start Month'], bins = 100, figsize = (20,6))
plt.hlines(y = average, xmin = 0, xmax= 12)
plt.show()

# for i in xrange(12):
#     month[i] = (len(conf_erup2014[conf_erup2014['Start Month'] == i+1]['Start Month'])-average)
# plt.bar([1,2,3,4,5,6,7,8,9,10,11,12],month )
# plt.show()


# In[252]:

conf_erup['Start Year'].min()
o_conf_erup = conf_erup
print conf_erup.columns

#determine what is needed on chart -- then graph it and turn it into bins
def makeChart(df,groupby_col,x_col_lst,y_col_lst,maxbars,numbars,startDate,endDate, binsize, use_rel_size)
    df.groupby[groupby_col]
    
#obj - show fatalaties vs global volcanicy for possive/active mdode for visualluy exploring data.


# In[227]:

from datetime import datetime

#previous error occurred due to leap year. 'Start Day' == 29 on row 6724 
#update affected row with 28 instead of 29 
conf_erup[conf_erup['Start Month']==2].replace(29,28,inplace=True)
#print conf_erup[(conf_erup['Start Month']==2) & (conf_erup['Start Day']==29)]
conf_erup = o_conf_erup
conf_erup['Start Date'] = conf_erup.apply(lambda row: datetime(int(row['Start Year']), int(row['Start Month']), int(row['Start Day'])), axis=1)
conf_erup.head()


# In[ ]:

#Look at the End Years - notice the NAN
conf_erup['End Year'].unique()

#675 values are null for End Year
print conf_erup[conf_erup['End Year'].isnull()].shape 

#determine which samples have a complete Year, Month, Day for End
not_null_end_dates = conf_erup[conf_erup['End Month'].notnull() & conf_erup['End Year'].notnull() & conf_erup['End Day'].notnull()]
print not_null_end_dates.shape

#isolate to these samples to a new data frame and determine the average amount of time between eruption start and end time
date_comp = conf_erup[conf_erup['End Month'].notnull() & conf_erup['End Year'].notnull() &  conf_erup['End Day'].notnull()]

#error occurred when attempting to convert Year, Month, Day to datetime below because some days have 0 for End Day
#determine the amount of samples that have 0 for end day
print date_comp[date_comp['End Day']==0].shape #409 values have 0 for the day


#make the day for all these samples to be 1
zero_days = date_comp[date_comp['End Day']==0].index
for i in zero_days:
    date_comp.ix[i,'End Day']=1

#error occurred because one of the months were 0
#print date_comp.ix[920]
print date_comp[date_comp['End Month']==0].shape #60 samples have an End Month==0

zero_months = date_comp[date_comp['End Month']==0].index
for i in zero_months:
    date_comp.ix[i,'End Month']=1
    
#now convert samples and create End Date column
def convert_dates(conf_erup):
    conf_erup['End Date'] = conf_erup.apply(lambda row: datetime(int(row['End Year']), int(row['End Month']), int(row['End Day'])), axis=1)
    return conf_erup

df = convert_dates(date_comp)
df.head()
#Yay!


# In[213]:

df


# In[225]:

len(df[(df['Start Month']>=4) & (df['Start Month']<=12)])#.hist(bins=10)


# In[115]:

def remove_zero(date_comp):
    zero_days = date_comp[date_comp['End Day']==0].index
    for i in zero_days:
        date_comp.ix[i,'End Day']=1

    zero_months = date_comp[date_comp['End Month']==0].index
    for i in zero_months:
        date_comp.ix[i,'End Month']=1
    return date_comp


# In[177]:


#now we want to determine the average amount of time between start and end for a volcano so we can impute the values that don't exist
print np.sum(df['End Date']-df['Start Date'])

#now get the mean
print 1019/float(len(df))
eruption_days = convert = [(a.astype('timedelta64[D]')).astype(float) for a in abs_dev.values]
df_mean = np.mean(eruption_days)
df_std = np.std(eruption_days)

print df_mean
print df_std

import datetime as dt

#Now we can impute dates for start and end date that normally distributed according to the mean and std indicated above
#distributed with a mean and std deviation as seen above

#select all data that does not have complete start and end dates and create a value that will not bias our sample
conf_erup[conf_erup['End Year'].isnull() | conf_erup['End Month'].isnull() | conf_erup['End Day'].isnull()].shape 

#676 with null value in either Year, Month, Date
not_null = conf_erup[conf_erup['End Year'].notnull() & conf_erup['End Month'].notnull() & conf_erup['End Day'].notnull()] 
conf_erup[conf_erup['End Year'].notnull() & conf_erup['End Month'].notnull() & conf_erup['End Day'].notnull()] = convert_dates(not_null)

#removes 0s in month and day
conf_erup = remove_zero(conf_erup)

import numpy.random

#create End dates normally distrubuted according to mean and std
null_dates = conf_erup[conf_erup['End Year'].isnull() | conf_erup['End Month'].isnull() | conf_erup['End Day'].isnull()]
n = len(null_dates)
rand = [np.random.normal(df_mean,df_std) for r in np.arange(n)]
rand_days=[]
for r in rand:
    if r<0:
        rand_days.append(0)
    else:
        rand_days.append(r)

new_days = [a+dt.timedelta(days=r) for (a,r) in zip(null_dates['Start Date'],rand_days)]

assert(len(null_dates)==len(new_days))
null_dates['End Date'] = new_days

#merge null_dates with conf_erup
conf_erup.ix[conf_erup.index.isin(null_dates.index),'End Date'] = null_dates['End Date']

conf_erup['End Date']




# In[ ]:

"""
This example shows how to use a path patch to draw a bunch of
rectangles for an animated histogram
"""
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation
from matplotlib import interactive
interactive(True)


fig, ax = plt.subplots()

# histogram our data with numpy
data = np.random.randn(1000)
n, bins = np.histogram(data, 100)

# get the corners of the rectangles for the histogram
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n
nrects = len(left)

# here comes the tricky part -- we have to set up the vertex and path
# codes arrays using moveto, lineto and closepoly

# for each rect: 1 for the MOVETO, 3 for the LINETO, 1 for the
# CLOSEPOLY; the vert for the closepoly is ignored but we still need
# it to keep the codes aligned with the vertices
nverts = nrects*(1+3+1)
verts = np.zeros((nverts, 2))
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5,0] = left
verts[0::5,1] = bottom
verts[1::5,0] = left
verts[1::5,1] = top
verts[2::5,0] = right
verts[2::5,1] = top
verts[3::5,0] = right
verts[3::5,1] = bottom

barpath = path.Path(verts, codes)
patch = patches.PathPatch(barpath, facecolor='green', edgecolor='yellow', alpha=0.5)
ax.add_patch(patch)

ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())

def animate(i):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, bins = np.histogram(data, 100)
    top = bottom + n
    verts[1::5,1] = top
    verts[2::5,1] = top

ani = animation.FuncAnimation(fig, animate, 100, repeat=False)
plt.show()


# In[ ]:



