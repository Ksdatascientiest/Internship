#!/usr/bin/env python
# coding: utf-8

# In[67]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[68]:


sns.set_style('darkgrid')
plt.rcParams['font.size'] = 15
plt.rcParams['figure.figsize'] = (10, 7)
plt.rcParams['figure.facecolor'] = '#FFE584'


# In[105]:


data = pd.read_csv('C:\\Users\\erkai\\Downloads\\happiness_score_dataset.csv')


# In[117]:


data.head()


# In[118]:


data_columns = ['Country', 'Region', 'Happiness Rank', 'Happiness Score', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity','Dystopia Residual']


# In[119]:


data = data[data_columns].copy()


# In[144]:


happy_df = data.rename({'Country':'country_name', 'Region':'region', 'Happiness Score':'happiness_score', 'Economy (GDP per Capita)':'Economy_GDP_per_Capita', 'Family':'family', 'Health (Life Expectancy)':'Health_Life_Expectancy', 'Freedom':'freedom', 'Trust (Government Corruption)':'Trust_Government_Corruption' },axis =1)


# In[145]:


happy_df.head()


# In[146]:


happy_df.isnull().sum()


# In[88]:


#Plot between happiness and GDP


plt.rcParams['figure.figsize'] = (15, 7)
plt.title('plot between Happiness Score and GDP')
sns.scatterplot(x = happy_df.happiness_score, y = happy_df.Economy_GDP_per_Capita, hue = happy_df.region, s = 200);

plt.legend(loc = 'upper left', fontsize = '10')
plt.xlabel('Happiness Score')
plt.ylabel('GDP per capita')


# In[90]:


gdp_region = happy_df.groupby('region')['Economy_GDP_per_Capita'].sum()
gdp_region


# In[91]:


gdp_region.plot.pie(autopct = '%1.1f%%')
plt.title('GDP by Region')
plt.ylabel('')


# In[94]:


# total countries

total_country = happy_df.groupby('region')[['country_name']].count()
print(total_country)


# In[99]:


# Correlation Map

cor = happy_df.corr(method = "pearson")
f, ax = plt.subplots(figsize = (10, 5))
sns.heatmap(cor, mask = np.zeros_like(cor, dtype =np.bool),
            cmap= "Blues", square=True, ax=ax)


# In[130]:


# Corruption in region

corruption = happy_df.groupby('region')[['Trust_Government_Corruption']].mean()
corruption


# In[132]:


plt.rcParams['figure.figsize'] = (12, 8)
plt.title('Perception of Corruption in various Region')
plt.xlabel('Regions', fontsize = 15)
plt.ylabel('Corruption Index', fontsize = 15)
plt.xticks(rotation = 30, ha = 'right')
plt.bar(corruption.index, corruption.Trust_Government_Corruption)


# In[154]:


top_10 = happy_df.head(10)
bottom_10 = happy_df.tail(10)


# In[155]:


fig, axes = plt.subplots(1, 2, figsize= (16, 6))
plt.tight_layout(pad= 2)
xlabel = top_10.country_name
axes[0].set_title('Top 10 happiest countries life Expectancy')
axes[0].set_xticklabels(xlabel, rotation=45, ha='right')
sns.barplot(x= top_10.country_name, y=top_10.Health_Life_Expectancy, ax=axes[0])
axes[0].set_xlabel('country Name')
axes[0].set_ylabel('Health_Life_Expectancy')

xlabels= bottom_10.country_name
axes[1].set_title('Bottom 10 least happy countries life exceptancy')
axes[1].set_xticklabels(xlabel, rotation = 45, ha='right')
sns.barplot(x= bottom_10.country_name, y= bottom_10.Health_Life_Expectancy, ax=axes[1])
axes[1].set_xlabel('Country Name')
axes[1].set_ylabel('Health_Life_Expectancy')


# In[157]:


plt.rcParams['figure.figsize'] = (15, 7)
sns.scatterplot(x= happy_df.freedom, y=happy_df.happiness_score, hue= happy_df.region, s = 200)
plt.legend(loc = 'upper left', fontsize = '12')
plt.xlabel('freedom')
plt.ylabel('Happiness Score')


# In[165]:


country = happy_df.sort_values(by= 'Trust_Government_Corruption').head(10)
plt.rcParams['figure.figsize'] = (12, 6)
plt.title('Countries with most Perception of corruption')
plt.xlabel('Country', fontsize = 13)
plt.ylabel('Corruption index', fontsize= 13)
plt.xticks(rotation = 30, ha= 'right')
plt.bar(country.country_name,  country.Trust_Government_Corruption)


# In[ ]:


#corruption vs happiness


