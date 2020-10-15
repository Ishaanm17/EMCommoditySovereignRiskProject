#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

PR=pd.read_excel (r"C:\New folder\Political Risk Data 10-10-2020.xlsx")

PR


# In[5]:


PR=PR.set_index('Year')


# In[6]:


PR


# In[7]:


list(PR.columns)


# In[8]:


PR.mean(axis='columns')


# In[9]:


import matplotlib.pyplot as plt 

fig, ax= plt.subplots()
PR.mean(axis='columns').plot(ax=ax, label='mean')

PR.quantile(q=.25, axis='columns').plot(ax=ax, label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(ax=ax, label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(ax=ax, label='75%', color='k', linestyle='--')
PR['India'].plot(ax=ax, color='red')

ax.set_title('India vs EM Peers Political Risk')
ax.set_ylabel('Political Risk (ICRG)')
ax.set_xlabel('Year')

ax.legend(loc='best')


# In[10]:


fig, ax= plt.subplots()
PR.mean(axis='columns').plot(ax=ax, label='mean')

PR.quantile(q=.25, axis='columns').plot(ax=ax, label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(ax=ax, label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(ax=ax, label='75%', color='k', linestyle='--')
PR['Argentina'].plot(ax=ax, color='red')

ax.set_title('Argentina vs EM Peers Political Risk')
ax.set_ylabel('Political Risk (ICRG)')
ax.set_xlabel('Year')

ax.legend(loc='best')


# In[11]:


fig, ax= plt.subplots()
PR.mean(axis='columns').plot(ax=ax, label='mean')

PR.quantile(q=.25, axis='columns').plot(ax=ax, label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(ax=ax, label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(ax=ax, label='75%', color='k', linestyle='--')
PR['China'].plot(ax=ax, color='red')

ax.set_title('China vs EM Peers Political Risk')
ax.set_ylabel('Political Risk (ICRG)')
ax.set_xlabel('Year')

ax.legend(loc='best')


# In[12]:


ER=pd.read_excel (r"C:\New folder\Economic Risk Data 10-10-2020.xlsx")

ER


# In[13]:


ER=ER.set_index('Year')


# In[14]:


fig, ax= plt.subplots()
ER.mean(axis='columns').plot(ax=ax, label='mean')

ER.quantile(q=.25, axis='columns').plot(ax=ax, label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(ax=ax, label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(ax=ax, label='75%', color='k', linestyle='--')
ER['India'].plot(ax=ax, color='red')

ax.set_title('India vs EM Peers Economic Risk')
ax.set_ylabel('Economic Risk (ICRG)')
ax.set_xlabel('Year')

ax.legend(loc='best')


# In[15]:


fig, ax= plt.subplots()
ER.mean(axis='columns').plot(ax=ax, label='mean')

ER.quantile(q=.25, axis='columns').plot(ax=ax, label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(ax=ax, label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(ax=ax, label='75%', color='k', linestyle='--')
ER['Argentina'].plot(ax=ax, color='red')

ax.set_title('Argentina vs EM Peers Economic Risk')
ax.set_ylabel('Economic Risk (ICRG)')
ax.set_xlabel('Year')

ax.legend(loc='best')


# In[16]:


fig, ax= plt.subplots()
ER.mean(axis='columns').plot(ax=ax, label='mean')

ER.quantile(q=.25, axis='columns').plot(ax=ax, label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(ax=ax, label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(ax=ax, label='75%', color='k', linestyle='--')
ER['China'].plot(ax=ax, color='red')

ax.set_title('China vs EM Peers Economic Risk')
ax.set_ylabel('Economic Risk (ICRG)')
ax.set_xlabel('Year')

ax.legend(loc='best')


# In[17]:


SR=pd.read_excel (r"C:\New folder\Sovereign Risk Data 10-10-2020.xlsx")

SR


# In[18]:


SR=SR.set_index('Year')


# In[19]:


fig, ax= plt.subplots()
SR.mean(axis='columns').plot(ax=ax, label='mean')

SR.quantile(q=.25, axis='columns').plot(ax=ax, label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(ax=ax, label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(ax=ax, label='75%', color='k', linestyle='--')
SR['India'].plot(ax=ax, color='red')

ax.set_title('India vs EM Peers Sovereign Risk')
ax.set_ylabel('Sovereign Risk (ICRG)')
ax.set_xlabel('Year')

ax.legend(loc='best')


# In[20]:


fig, ax= plt.subplots()
SR.mean(axis='columns').plot(ax=ax, label='mean')

SR.quantile(q=.25, axis='columns').plot(ax=ax, label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(ax=ax, label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(ax=ax, label='75%', color='k', linestyle='--')
SR['Argentina'].plot(ax=ax, color='red')

ax.set_title('Argentina vs EM Peers Sovereign Risk')
ax.set_ylabel('Sovereign Risk (ICRG)')
ax.set_xlabel('Year')

ax.legend(loc='best')


# In[21]:


fig, ax= plt.subplots()
SR.mean(axis='columns').plot(ax=ax, label='mean')

SR.quantile(q=.25, axis='columns').plot(ax=ax, label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(ax=ax, label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(ax=ax, label='75%', color='k', linestyle='--')
SR['China'].plot(ax=ax, color='red')

ax.set_title('China vs EM Peers Sovereign Risk')
ax.set_ylabel('Sovereign Risk (ICRG)')
ax.set_xlabel('Year')

ax.legend(loc='best')


# #### Comparing Each Individual EM with their repsective peers 

# In[67]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax1,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax1,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax1,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax1,  label='mean')
PR['Argentina'].plot(x='Year', y='Political Risk',ax=ax1,  color='red')
ax1.set_title("Argentina vs EM Peers Political Risk", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax2,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax2,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax2,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax2,  label='mean')
PR['Brazil'].plot(x='Year', y='Political Risk',ax=ax2,  color='red')
ax2.set_title("Brazil vs EM Peers Political Risk", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax3,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax3,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax3,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax3,  label='mean')
PR['China'].plot(x='Year', y='Political Risk',ax=ax3,  color='red')
ax3.set_title("China vs EM Peers Political Risk", fontsize=20)

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax4,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax4,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax4,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax4,  label='mean')
PR['Chile'].plot(x='Year', y='Political Risk',ax=ax4,  color='red')
ax4.set_title("Chile vs EM Peers Political Risk", fontsize=20)


# In[69]:


fig, ((ax5, ax6), (ax7, ax8)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax5,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax5,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax5,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax5,  label='mean')
PR['Colombia'].plot(x='Year', y='Political Risk',ax=ax5,  color='red')
ax5.set_title("Colombia vs EM Peers Political Risk", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax6,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax6,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax6,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax6,  label='mean')
PR['Egypt'].plot(x='Year', y='Political Risk',ax=ax6,  color='red')
ax6.set_title("Egypt vs EM Peers Political Risk", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax7,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax7,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax7,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax7,  label='mean')
PR['Hungary'].plot(x='Year', y='Political Risk',ax=ax7,  color='red')
ax7.set_title("Hungary vs EM Peers Political Risk", fontsize=20)

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax8,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax8,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax8,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax8,  label='mean')
PR['India'].plot(x='Year', y='Political Risk',ax=ax8,  color='red')
ax8.set_title("India vs EM Peers Political Risk", fontsize=20)


# In[70]:


fig, ((ax9, ax10), (ax11, ax12)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax9,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax9,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax9,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax9,  label='mean')
PR['Indonesia'].plot(x='Year', y='Political Risk',ax=ax9,  color='red')
ax9.set_title("Indonesia vs EM Peers Political Risk", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax10,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax10,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax10,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax10,  label='mean')
PR['Malaysia'].plot(x='Year', y='Political Risk',ax=ax10,  color='red')
ax10.set_title("Malaysia vs EM Peers Political Risk", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax11,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax11,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax11,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax11,  label='mean')
PR['Mexico'].plot(x='Year', y='Political Risk',ax=ax11,  color='red')
ax11.set_title("Mexico vs EM Peers Political Risk", fontsize=20)

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax12,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax12,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax12,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax12,  label='mean')
PR['Pakistan'].plot(x='Year', y='Political Risk',ax=ax12,  color='red')
ax12.set_title("Pakistan vs EM Peers Political Risk", fontsize=20)


# In[72]:


fig, ((ax13, ax14), (ax15, ax16)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax13,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax13,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax13,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax13,  label='mean')
PR['Peru'].plot(x='Year', y='Political Risk',ax=ax13,  color='red')
ax13.set_title("Peru vs EM Peers Political Risk", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax14,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax14,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax14,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax14,  label='mean')
PR['Philippines'].plot(x='Year', y='Political Risk',ax=ax14,  color='red')
ax14.set_title("Philippines vs EM Peers Political Risk", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax15,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax15,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax15,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax15,  label='mean')
PR['Poland'].plot(x='Year', y='Political Risk',ax=ax15,  color='red')
ax15.set_title("Poland vs EM Peers Political Risk", fontsize=20)

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax16,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax16,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax16,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax16,  label='mean')
PR['Qatar'].plot(x='Year', y='Political Risk',ax=ax16,  color='red')
ax16.set_title("Qatar vs EM Peers Political Risk", fontsize=20)


# In[75]:


fig, ((ax17, ax18), (ax19, ax20)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax17,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax17,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax17,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax17,  label='mean')
PR['Russia'].plot(x='Year', y='Political Risk',ax=ax17,  color='red')
ax17.set_title("Russia vs EM Peers Political Risk (1992-2016)", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax18,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax18,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax18,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax18,  label='mean')
PR['Saudi Arabia'].plot(x='Year', y='Political Risk',ax=ax18,  color='red')
ax18.set_title("Saudi Arabia vs EM Peers Political Risk", fontsize=20)


PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax19,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax19,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax19,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax19,  label='mean')
PR['South Africa'].plot(x='Year', y='Political Risk',ax=ax19,  color='red')
ax19.set_title("South Africa vs EM Peers Political Risk", fontsize=20)

PR.quantile(q=.25, axis='columns').plot(x='Year', y='Political Risk',ax=ax20,  label='25%', color='k', linestyle='--')
PR.median(axis='columns').plot(x='Year', y='Political Risk',ax=ax20,  label='median', color='gray', linestyle='--')
PR.quantile(q=.75, axis='columns').plot(x='Year', y='Political Risk',ax=ax20,  label='75%', color='k', linestyle='--')
PR.mean(axis='columns').plot(ax=ax20,  label='mean')
PR['Thailand'].plot(x='Year', y='Political Risk',ax=ax20,  color='red')
ax20.set_title("Thailand vs EM Peers Political Risk", fontsize=20)


# In[76]:


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax1,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax1,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax1,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax1,  label='mean')
ER['Argentina'].plot(x='Year', y='Economic Risk',ax=ax1,  color='red')
ax1.set_title("Argentina vs EM Peers Economic Risk", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax2,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax2,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax2,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax2,  label='mean')
ER['Brazil'].plot(x='Year', y='Economic Risk',ax=ax2,  color='red')
ax2.set_title("Brazil vs EM Peers Economic Risk", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax3,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax3,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax3,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax3,  label='mean')
ER['China'].plot(x='Year', y='Economic Risk',ax=ax3,  color='red')
ax3.set_title("China vs EM Peers Economic Risk", fontsize=20)

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax4,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax4,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax4,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax4,  label='mean')
ER['Chile'].plot(x='Year', y='Economic Risk',ax=ax4,  color='red')
ax4.set_title("Chile vs EM Peers Economic Risk", fontsize=20)


# In[77]:


fig, ((ax5, ax6), (ax7, ax8)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax5,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax5,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax5,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax5,  label='mean')
ER['Colombia'].plot(x='Year', y='Economic Risk',ax=ax5,  color='red')
ax5.set_title("Colombia vs EM Peers Economic Risk", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax6,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax6,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax6,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax6,  label='mean')
ER['Egypt'].plot(x='Year', y='Economic Risk',ax=ax6,  color='red')
ax6.set_title("Egypt vs EM Peers Economic Risk", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax7,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax7,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax7,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax7,  label='mean')
ER['Hungary'].plot(x='Year', y='Economic Risk',ax=ax7,  color='red')
ax7.set_title("Hungary vs EM Peers Economic Risk", fontsize=20)

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax8,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax8,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax8,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax8,  label='mean')
ER['India'].plot(x='Year', y='Economic Risk',ax=ax8,  color='red')
ax8.set_title("India vs EM Peers Economic Risk", fontsize=20)


# In[78]:


fig, ((ax9, ax10), (ax11, ax12)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax9,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax9,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax9,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax9,  label='mean')
ER['Indonesia'].plot(x='Year', y='Economic Risk',ax=ax9,  color='red')
ax9.set_title("Indonesia vs EM Peers Economic Risk", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax10,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax10,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax10,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax10,  label='mean')
ER['Malaysia'].plot(x='Year', y='Economic Risk',ax=ax10,  color='red')
ax10.set_title("Malaysia vs EM Peers Economic Risk", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax11,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax11,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax11,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax11,  label='mean')
ER['Mexico'].plot(x='Year', y='Economic Risk',ax=ax11,  color='red')
ax11.set_title("Mexico vs EM Peers Economic Risk", fontsize=20)

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax12,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax12,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax12,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax12,  label='mean')
ER['Pakistan'].plot(x='Year', y='Economic Risk',ax=ax12,  color='red')
ax12.set_title("Pakistan vs EM Peers Economic Risk", fontsize=20)


# In[79]:


fig, ((ax13, ax14), (ax15, ax16)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax13,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax13,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax13,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax13,  label='mean')
ER['Peru'].plot(x='Year', y='Economic Risk',ax=ax13,  color='red')
ax13.set_title("Peru vs EM Peers Economic Risk", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax14,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax14,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax14,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax14,  label='mean')
ER['Philippines'].plot(x='Year', y='Economic Risk',ax=ax14,  color='red')
ax14.set_title("Philippines vs EM Peers Economic Risk", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax15,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax15,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax15,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax15,  label='mean')
ER['Poland'].plot(x='Year', y='Economic Risk',ax=ax15,  color='red')
ax15.set_title("Poland vs EM Peers Economic Risk", fontsize=20)

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax16,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax16,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax16,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax16,  label='mean')
ER['Qatar'].plot(x='Year', y='Economic Risk',ax=ax16,  color='red')
ax16.set_title("Qatar vs EM Peers Economic Risk", fontsize=20)


# In[80]:


fig, ((ax17, ax18), (ax19, ax20)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax17,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax17,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax17,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax17,  label='mean')
ER['Russia'].plot(x='Year', y='Economic Risk',ax=ax17,  color='red')
ax17.set_title("Russia vs EM Peers Economic Risk (1992-2016)", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax18,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax18,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax18,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax18,  label='mean')
ER['Saudi Arabia'].plot(x='Year', y='Economic Risk',ax=ax18,  color='red')
ax18.set_title("Saudi Arabia vs EM Peers Economic Risk", fontsize=20)


ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax19,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax19,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax19,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax19,  label='mean')
ER['South Africa'].plot(x='Year', y='Economic Risk',ax=ax19,  color='red')
ax19.set_title("South Africa vs EM Peers Economic Risk", fontsize=20)

ER.quantile(q=.25, axis='columns').plot(x='Year', y='Economic Risk',ax=ax20,  label='25%', color='k', linestyle='--')
ER.median(axis='columns').plot(x='Year', y='Economic Risk',ax=ax20,  label='median', color='gray', linestyle='--')
ER.quantile(q=.75, axis='columns').plot(x='Year', y='Economic Risk',ax=ax20,  label='75%', color='k', linestyle='--')
ER.mean(axis='columns').plot(ax=ax20,  label='mean')
ER['Thailand'].plot(x='Year', y='Economic Risk',ax=ax20,  color='red')
ax20.set_title("Thailand vs EM Peers Economic Risk", fontsize=20)


# In[81]:


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax1,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax1,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax1,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax1,  label='mean')
SR['Argentina'].plot(x='Year', y='Sovereign Risk',ax=ax1,  color='red')
ax1.set_title("Argentina vs EM Peers Sovereign Risk", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax2,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax2,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax2,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax2,  label='mean')
SR['Brazil'].plot(x='Year', y='Sovereign Risk',ax=ax2,  color='red')
ax2.set_title("Brazil vs EM Peers Sovereign Risk", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax3,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax3,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax3,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax3,  label='mean')
SR['China'].plot(x='Year', y='Sovereign Risk',ax=ax3,  color='red')
ax3.set_title("China vs EM Peers Sovereign Risk", fontsize=20)

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax4,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax4,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax4,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax4,  label='mean')
SR['Chile'].plot(x='Year', y='Sovereign Risk',ax=ax4,  color='red')
ax4.set_title("Chile vs EM Peers Sovereign Risk", fontsize=20)


# In[82]:


fig, ((ax5, ax6), (ax7, ax8)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax5,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax5,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax5,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax5,  label='mean')
SR['Colombia'].plot(x='Year', y='Sovereign Risk',ax=ax5,  color='red')
ax5.set_title("Colombia vs EM Peers Sovereign Risk", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax6,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax6,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax6,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax6,  label='mean')
SR['Egypt'].plot(x='Year', y='Sovereign Risk',ax=ax6,  color='red')
ax6.set_title("Egypt vs EM Peers Sovereign Risk", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax7,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax7,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax7,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax7,  label='mean')
SR['Hungary'].plot(x='Year', y='Sovereign Risk',ax=ax7,  color='red')
ax7.set_title("Hungary vs EM Peers Sovereign Risk", fontsize=20)

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax8,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax8,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax8,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax8,  label='mean')
SR['India'].plot(x='Year', y='Sovereign Risk',ax=ax8,  color='red')
ax8.set_title("India vs EM Peers Sovereign Risk", fontsize=20)


# In[83]:


fig, ((ax9, ax10), (ax11, ax12)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax9,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax9,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax9,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax9,  label='mean')
SR['Indonesia'].plot(x='Year', y='Sovereign Risk',ax=ax9,  color='red')
ax9.set_title("Indonesia vs EM Peers Sovereign Risk", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax10,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax10,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax10,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax10,  label='mean')
SR['Malaysia'].plot(x='Year', y='Sovereign Risk',ax=ax10,  color='red')
ax10.set_title("Malaysia vs EM Peers Sovereign Risk", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax11,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax11,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax11,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax11,  label='mean')
SR['Mexico'].plot(x='Year', y='Sovereign Risk',ax=ax11,  color='red')
ax11.set_title("Mexico vs EM Peers Sovereign Risk", fontsize=20)

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax12,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax12,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax12,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax12,  label='mean')
SR['Pakistan'].plot(x='Year', y='Sovereign Risk',ax=ax12,  color='red')
ax12.set_title("Pakistan vs EM Peers Sovereign Risk", fontsize=20)


# In[85]:


fig, ((ax13, ax14), (ax15, ax16)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax13,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax13,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax13,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax13,  label='mean')
SR['Peru'].plot(x='Year', y='Sovereign Risk',ax=ax13,  color='red')
ax13.set_title("Peru vs EM Peers Sovereign Risk", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax14,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax14,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax14,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax14,  label='mean')
SR['Philippines'].plot(x='Year', y='Sovereign Risk',ax=ax14,  color='red')
ax14.set_title("Philippines vs EM Peers Sovereign Risk", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Soveriegn Risk',ax=ax15,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax15,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax15,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax15,  label='mean')
SR['Poland'].plot(x='Year', y='Sovereign Risk',ax=ax15,  color='red')
ax15.set_title("Poland vs EM Peers Sovereign Risk", fontsize=20)

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax16,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax16,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax16,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax16,  label='mean')
SR['Qatar'].plot(x='Year', y='Sovereign Risk',ax=ax16,  color='red')
ax16.set_title("Qatar vs EM Peers Sovereign Risk", fontsize=20)


# In[86]:


fig, ((ax17, ax18), (ax19, ax20)) = plt.subplots(nrows=2, ncols=2, sharex=True,  figsize=(15,5))

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax17,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax17,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax17,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax17,  label='mean')
SR['Russia'].plot(x='Year', y='Sovereign Risk',ax=ax17,  color='red')
ax17.set_title("Russia vs EM Peers Sovereign Risk (1992-2016)", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax18,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Soveriegn Risk',ax=ax18,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax18,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax18,  label='mean')
SR['Saudi Arabia'].plot(x='Year', y='Sovereign Risk',ax=ax18,  color='red')
ax18.set_title("Saudi Arabia vs EM Peers Sovereign Risk", fontsize=20)


SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax19,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax19,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax19,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax19,  label='mean')
SR['South Africa'].plot(x='Year', y='Sovereign Risk',ax=ax19,  color='red')
ax19.set_title("South Africa vs EM Peers Sovereign Risk", fontsize=20)

SR.quantile(q=.25, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax20,  label='25%', color='k', linestyle='--')
SR.median(axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax20,  label='median', color='gray', linestyle='--')
SR.quantile(q=.75, axis='columns').plot(x='Year', y='Sovereign Risk',ax=ax20,  label='75%', color='k', linestyle='--')
SR.mean(axis='columns').plot(ax=ax20,  label='mean')
SR['Thailand'].plot(x='Year', y='Sovereign Risk',ax=ax20,  color='red')
ax20.set_title("Thailand vs EM Peers Sovereign Risk", fontsize=20)


# In[ ]:




