


# importing needed libraries 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import wbgapi as wb
import seaborn as sns
import warnings
warnings.filterwarnings("ignore") 


# In[26]:


country_codes = ["GBR","USA","IND","JPN","RUS","CHN"]
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]


# In[27]:


"""This function helps us to get data from world bank api and we are performing transpose inbuilt function to
get countries as columns"""
def get_data(indicator, codes, years):
    data = wb.data.DataFrame(indicator, codes, time = years, labels=True).drop('Country', 1)
    data1 = data.rename_axis(index = "countries")
    transposed_data = data1.transpose().iloc[1: , :]
    
    return data1, transposed_data


# In[45]:


#indicators fetched from world bank api
indicators = {"agriculture land":"AG.LND.AGRI.ZS",
              "arable land":"AG.LND.ARBL.ZS",
              "co2":"EN.ATM.CO2E.KT",
              "energy production": "EG.ELC.NGAS.ZS",
              "energy production through oil": "EG.ELC.FOSL.ZS",
              "energy production through coal":"EG.ELC.COAL.ZS",}


# ### Acessing data and plotting graphs

# In[46]:


#accessing forest land data
agri, agri_land_T = get_data(indicators["agriculture land"], country_codes, years)


# In[30]:


# accessing arable land data
arable_land, arable_land_T = get_data(indicators["arable land"], country_codes, years)


# In[83]:


agri.mean()


# In[81]:


agri.loc["CHN"].mean()


# In[98]:


#comparing various countries forest land
agri_land_T.mean().plot.barh(figsize = (16,8), width = 0.5, edgecolor = "Black")
plt.title("Comparing values of Agriculture land for different countries", fontsize = 15)
plt.ylabel("countries", fontsize = 14)
plt.show()


# In[99]:


#comparing various countries arable land
arable_land_T.mean().plot.barh(figsize = (16,8), width = 0.5, edgecolor = "Black")
plt.title("Comparing values of Arable land for different countries", fontsize = 15)
plt.ylabel("countries", fontsize = 14)
plt.show()


# In[36]:


# accessing data for other indicators
co2, co2_T = get_data(indicators["co2"], country_codes, years)
en_prod, en_prod_T = get_data(indicators["energy production"], country_codes, years)
en_oil, en_oil_T = get_data(indicators["energy production through oil"], country_codes, years)
en_coal, en_coal_T = get_data(indicators["energy production through coal"], country_codes, years)


# In[37]:


# storing the columns name as a list, which can be used as labels
le = co2_T.columns 


# In[38]:


le


# In[97]:


#comparing energy production values from different resources 
fig, ax = plt.subplots(figsize = (16,6))
ax.plot(en_prod.loc["GBR"], label="Energy Production",marker = 'o')
ax.plot(en_oil.loc["GBR"], label="Energy Production using Oil, Gas & Coal",marker = 'o')
ax.plot(en_coal.loc["GBR"], label="Energy Production Coal",marker = 'o')

ax.grid()

ax.legend(loc='upper right')
ax.set_title("energy production from various sources", fontsize = 16)
ax.set_ylabel("Energy production", fontsize = 12)

plt.show()


# In[96]:


#comparing co2 emissions accross countries
plt.figure(figsize=[16,6])
plt.plot(co2_T, marker = 'o')
plt.xlabel("year")
plt.ylabel("CO2 emissions (kt)", fontsize = 12)
plt.title("Co2 Emissions", fontsize = 16)
plt.legend(labels = le, loc = 1)
plt.grid()
plt.show()


# In[52]:


# heatmap for co2 accross countries
co2_corr = co2_T.corr()
sns.heatmap(co2_corr,cmap = "Blues", annot = True)
plt.show()


# In[ ]:




