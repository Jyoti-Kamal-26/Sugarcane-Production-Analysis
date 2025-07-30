#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


df=pd.read_csv('List of Countries by Sugarcane Production.csv')


# In[7]:


df=pd.read_csv('List of Countries by Sugarcane Production.csv')


# In[8]:


df.head()


# In[9]:


df.shape


# ### Data Cleaning

# In[10]:


df['Production (Tons)']=df['Production (Tons)'].str.replace('.','')
df['Production per Person (Kg)']=df['Production per Person (Kg)'].str.replace('.','').str.replace(',','.')
df['Acreage (Hectare)']=df['Acreage (Hectare)'].str.replace('.','')
df['Yield (Kg / Hectare)']=df['Yield (Kg / Hectare)'].str.replace('.','').str.replace(',','.')


# In[11]:


df.head()


# In[12]:


df.rename(columns={'Production (Tons)':'Production(Tons)'},inplace=True)
df.rename(columns={'Production per Person (Kg)':'Production_per_Person(Kg)'},inplace=True)
df.rename(columns={'Acreage (Hectare)':'Acreage(Hectare)'},inplace=True)
df.rename(columns={'Yield (Kg / Hectare)':'Yield(Kg/Hectare)'},inplace=True)


# In[13]:


df.head()


# In[14]:


df.isna().sum()


# In[15]:


df[df['Acreage(Hectare)'].isnull()]


# In[16]:


df=df.dropna().reset_index()


# In[17]:


df.head()


# In[18]:


df.drop(['index','Unnamed: 0'], axis=1, inplace = True)


# In[19]:


df.head()


# In[20]:


df['Production(Tons)']=df['Production(Tons)'].astype(float)
df['Production_per_Person(Kg)']=df['Production_per_Person(Kg)'].astype(float)
df['Acreage(Hectare)']=df['Acreage(Hectare)'].astype(float)
df['Yield(Kg/Hectare)']=df['Yield(Kg/Hectare)'].astype(float)


# In[21]:


df.dtypes


# ### Univariate Analysis

# In[22]:


df.head()


# ### How many countries produce sugarcane from each contient?

# In[23]:


df['Continent'].value_counts()


# ### Distribution of the columns

# In[24]:


df['Continent'].value_counts().plot(kind='bar')


# ### Checking Outliers

# In[25]:


plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
sns.distplot(df['Production(Tons)'])

plt.subplot(2,2,2)
sns.distplot(df['Production_per_Person(Kg)'])

plt.subplot(2,2,3)
sns.distplot(df['Acreage(Hectare)'])

plt.subplot(2,2,4)
sns.distplot(df['Yield(Kg/Hectare)'])


# In[26]:


plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
sns.boxplot(df['Production(Tons)'])

plt.subplot(2,2,2)
sns.boxplot(df['Production_per_Person(Kg)'])

plt.subplot(2,2,3)
sns.boxplot(df['Acreage(Hectare)'])

plt.subplot(2,2,4)
sns.boxplot(df['Yield(Kg/Hectare)'])


# In[27]:


df.describe()


# ### Bivariate Analysis

# In[28]:


df.head()


# ### Which coountry produces maximum sugarcane?

# In[29]:


df_new=df[['Country','Production(Tons)']].set_index('Country')


# In[30]:


df_new


# In[31]:


df_new['Production(Tons)_percent']=df_new['Production(Tons)']*100/df_new['Production(Tons)'].sum()


# In[32]:


df_new


# In[33]:


df_new['Production(Tons)_percent'].plot(kind='pie',autopct='%.2f')


# In[34]:


df_new['Production(Tons)'].head(10).plot(kind='bar',color=plt.cm.get_cmap('tab10',10).colors)


# In[35]:


ax=sns.barplot(data=df.head(10),x='Country', y='Production(Tons)')
ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
plt.show()


# ### Which Country has highest land

# In[36]:


df_acr=df.sort_values('Acreage(Hectare)', ascending=False)
ax=sns.barplot(data=df_acr.head(10),x='Country', y='Acreage(Hectare)')
ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
plt.show()


# ### Which country has highest yield per hectare?

# In[37]:


df_yield=df.sort_values('Yield(Kg/Hectare)', ascending=False)
ax=sns.barplot(data=df_yield.head(10),x='Country', y='Yield(Kg/Hectare)')
ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
plt.show()


# ### Which country has highest production?

# In[38]:


df_prod=df.sort_values('Production_per_Person(Kg)', ascending=False)
ax=sns.barplot(data=df_prod.head(10),x='Country', y='Production_per_Person(Kg)')
ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
plt.show()


# ### Correlation

# In[39]:


corr_columns = df[['Production(Tons)', 'Production_per_Person(Kg)', 'Acreage(Hectare)','Yield(Kg/Hectare)']]
corr_columns.corr()


# In[40]:


sns.heatmap(corr_columns.corr(), annot=True, cmap='Greens')


# ### Do countries with highest land produse more sugarcane?

# In[41]:


sns.scatterplot(data=df, x='Acreage(Hectare)',y='Production(Tons)')


# ### Do countries which yield more sugarcane per hectare produces more sugarcane in total?

# In[42]:


sns.scatterplot(data=df, x='Yield(Kg/Hectare)',y='Production(Tons)')


# ### Analysis for Continent

# In[43]:


df_continent=df.groupby('Continent').sum()


# In[44]:


df_continent


# ### Which continent produces maximum sugarcane?

# In[45]:


df['Continent'].value_counts()


# In[46]:


df_continent['Production(Tons)'].sort_values(ascending=False).plot(kind='bar')


# In[47]:


df_continent['Acreage(Hectare)'].sort_values(ascending=False).plot(kind='bar')


# ### Do number of countries in a Continent effects production of sugarcane?

# In[48]:


df_continent['number_of_countries']=df.groupby('Continent').count()['Country']


# In[49]:


df_continent


# In[50]:


continent_names=df_continent.index.to_list()
sns.lineplot(data=df_continent, x='number_of_countries',y='Production(Tons)',color='Purple')
plt.xticks(df_continent['number_of_countries'],continent_names,rotation=90)
plt.show()


# ### Production distribution by continent

# In[51]:


df_continent['Production(Tons)'].plot(kind='pie',autopct='%.2f')


# ### Correlation Continent

# In[53]:


#correlation of fd_continent_columns
corr_continent_columns = df_continent[['Production(Tons)', 'Production_per_Person(Kg)', 'Acreage(Hectare)','Yield(Kg/Hectare)','number_of_countries']]
corr_continent_columns.corr()


# In[ ]:




