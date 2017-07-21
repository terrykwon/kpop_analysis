
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns


# In[2]:

import matplotlib.font_manager

# Configure matplotlib fonts.
matplotlib.font_manager.get_fontconfig_fonts()
font_location = "/Users/terrykwon/Library/Fonts/NotoSansCJKkr-Bold.otf"
font_name = matplotlib.font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name, weight='medium')
matplotlib.rc('axes', labelweight='medium', titleweight='medium')


# In[3]:

df = pd.read_csv('data/preprocessed_2.csv')

# Replace NaN with blank strings.
df = df.where((pd.notnull(df)), '')

df.head(30)


# In[4]:

# Plot distribution of song length.
fig = plt.subplots()[0]
fig.set_size_inches(15, 15)

ax = sns.distplot(df['time'], norm_hist=True)
ax.set_title('Distribution of song length', fontsize=20)
ax.set_xlabel('time(seconds)')
ax.tick_params(labelsize=18)
# ax.set_ylabel('proportion')


# In[5]:

# See how many songs make multiple appearances.
id_counter = Counter(df['id'])
id_counter.most_common(18)


# In[6]:

frequent_ids = [x[0] for x in id_counter.most_common(18)]
df.loc[df['id'].isin(frequent_ids)]


# In[7]:

artists = ','.join(df['artist']).split(',')
len(artists)


# In[8]:

artist_counter = Counter(artists)
artist_counter.most_common(30)


# In[9]:

artist_counts = list(artist_counter.values())


# In[10]:

# Plot distribution of artist counts
fig = plt.subplots()[0]
fig.set_size_inches(15, 10)
plt.axis([1, 35, 0, 0.6])
plt.title('Artist appearances on top 100 charts (2008-2016)', fontsize=22)
ax = sns.distplot(artist_counts, norm_hist=True, kde=False, color='red')
plt.xlabel('Appearances on chart', fontsize=20)
plt.ylabel('Proportion of total', fontsize=20)
ax.tick_params(labelsize=18)

# plt.savefig('artist-appearances.png', transparent=False, bbox_inches='tight')


# In[11]:

# Plot bar chart of artists in top 100
frequent_artists = artist_counter.most_common(34)
frequent_artists_x = [x[0] for x in frequent_artists]
frequent_artists_y = [x[1] for x in frequent_artists]

# sns.set(style="whitegrid")

fig = plt.subplots()[0]
fig.set_size_inches(15, 30)
ax = sns.barplot(x=frequent_artists_y, y=frequent_artists_x, orient='h')

plt.title('No. songs in Top 100 chart by artist (2008-2016)', y=1.03, fontsize=22)
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top
ax.tick_params(labeltop=True)
ax.tick_params(labelsize=18)

# plt.savefig('fig2-1.png', transparent=False, bbox_inches='tight')


# In[18]:

df.loc[df['rank'] <= 10]


# In[12]:

composers = ','.join(df['composer']).split(',')
composers = list(filter(lambda x: x != '', composers))
len(composers)


# In[13]:

composer_counter = Counter(composers)
composer_counter.most_common(47)


# In[14]:

# Plot bar chart of composers in top 100
frequent_composers = composer_counter.most_common(47)
frequent_composers_x = [x[0] for x in frequent_composers]
frequent_composers_y = [x[1] for x in frequent_composers]

fig, ax = plt.subplots()
fig.set_size_inches(15, 35)

ax = sns.barplot(x=frequent_composers_y, y=frequent_composers_x)

plt.title('No. songs in Top 100 chart by composer (2008-2016)', y=1.03, fontsize=22)
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top
ax.tick_params(labeltop=True)
ax.tick_params(labelsize=18)

# plt.savefig('fig3-1.png', transparent=False, bbox_inches='tight')


# In[15]:

lyricists = ','.join(df['lyricist']).split(',')
lyricists = list(filter(lambda x: x != '', lyricists))
len(lyricists)


# In[16]:

lyricist_counter = Counter(lyricists)
lyricist_counter.most_common(30)


# In[17]:

# Plot bar chart of composers in top 100
frequent_lyricists = lyricist_counter.most_common(42)
frequent_lyricists_x = [x[0] for x in frequent_lyricists]
frequent_lyricists_y = [x[1] for x in frequent_lyricists]

fig, ax = plt.subplots()
fig.set_size_inches(15, 35)

ax = sns.barplot(x=frequent_lyricists_y, y=frequent_lyricists_x)

plt.title('No. songs in Top 100 chart by lyricist (2008-2016)', y=1.03, fontsize=22)
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top
ax.tick_params(labeltop=True)
ax.tick_params(labelsize=18)

# plt.savefig('fig4-1.png', transparent=False, bbox_inches='tight')



