
# coding: utf-8

# In[288]:


import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt


# In[289]:


path = r'C:\Users\Pavan\Desktop\Rinteger\Guruchethan\Flipkart\Weekday\12-15\overall'
filesoverall = glob.glob(path+"/*.csv")


# In[290]:


dfs1 = []
for filename in filesoverall:
    dfs1.append(pd.read_csv(filename,index_col=None,header=1))


# In[291]:


overallframe = pd.concat(dfs1,axis=0, ignore_index=True)


# In[292]:


overallframe.head()


# In[293]:


path1 = r'C:\Users\Pavan\Desktop\Rinteger\Guruchethan\Flipkart\Weekday\12-15\Daily'
filesname = glob.glob(path1+"/*.csv")


# In[294]:


dfs = []
for filename in filesname:
    dfs.append(pd.read_csv(filename,index_col=None,header=1))


# In[295]:


dailyframe = pd.concat(dfs,axis=0, ignore_index=True)


# In[296]:


dailyframe.head()


# In[297]:


overallframe.shape


# In[298]:


overallframe.describe()


# In[299]:


dailyframe.shape


# In[300]:


dailyframe.head()


# In[301]:


listings = overallframe['Listing ID'].unique().tolist()


# In[302]:


listings


# In[303]:


framenew = pd.DataFrame(overallframe, columns = ['Listing ID', 'Sku Id'])


# In[304]:


framenew


# In[305]:


df_merge = pd.merge(dailyframe,framenew, on='Listing ID')


# In[306]:


df_merge


# In[307]:


df_merge.shape


# In[308]:


df_merge.drop(['Listing ID','Same FSN Orders','Same FSN Revenue (Rs.)','Other FSN Orders','Other FSN Revenue (Rs.)'],axis=1,inplace=True)


# In[309]:


df_merge


# In[316]:


df_merge = df_merge.assign(ClientName='Guruchethan',Marketplace = 'Flipkart',CPC=0)


# In[319]:


df_merge.head()


# In[ ]:


## Amazon data manipulation


# In[260]:


path = r'C:\Users\Pavan\Desktop\Rinteger\Guruchethan\1Mar - 4mar\Amazon'
allfilesamaz = glob.glob(path+"/*.csv") ## reading all the files at once with single code


# In[261]:


dfs_ama = []
for filename in allfilesamaz:
    dfs_ama.append(pd.read_csv(filename,index_col=None,header=0))


# In[262]:


frame_amazon = pd.concat(dfs_ama,axis=0,ignore_index=True)


# In[263]:


frame_amazon


# In[322]:


frame_amaz = frame_amazon.assign(ClientName='Guruchethan',CampaignId='GCMAR121519',Date = 'Mar 12-15',Marketplace='Amazon')


# In[323]:


frame_amaz


# In[324]:


frame_amaz.drop(['State','Status','ASIN'],axis=1,inplace=True)


# In[325]:


frame_amaz


# In[326]:


frame_amaz.rename(columns={'Products':'AdgroupName','SKU':'Sku Id','Impressions':'Views','Clicks':'Actions',
                                         'CTR(%)':'Action Rate (AR)(%)','Spend(INR)':'Budget Spent (Rs.)','Orders':'Total Orders',
                                        'Sales(INR)':'Total Revenue (Rs.)','ACOS(%)':'ROI','CPC(INR)':'CPC'},inplace = True)


# In[327]:


frame_amaz


# In[336]:


data_final = pd.concat([df_merge,frame_amaz],sort=True,ignore_index=True)


# In[337]:


data_final.shape


# In[339]:


data_final.isnull().sum()


# In[340]:


data_final.to_csv(r'C:\Users\Pavan\Desktop\Rinteger\Guruchethan\Final\finadata.csv')

