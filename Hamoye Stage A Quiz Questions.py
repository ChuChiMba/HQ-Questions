#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the pandas library and reading the dataset to a dataframe
import pandas as pd
data = pd.read_csv(r"C:\Users\Chinenye Claire\Downloads\FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding = "latin-1")
data.head()


# In[2]:


data.shape


# In[3]:


#random sampling of the dataset
data.sample(10)


# In[5]:


#getting the descriptive statistics foe each numerical column
data.describe()


# In[6]:


#getting the unique values in the Element column
data['Element'].unique()


# In[8]:


#getting the unique values in the Item column
data['Item'].unique()


# In[ ]:


Answering The Quiz Questions


# In[9]:


#Perform a groupby operation on ‘Element’.  What is the total number of the sum of Processing in 2017?
Answer = data.groupby('Element').sum().loc['Processing']['Y2017']
print('The sum of processing in 2017 is', (Answer))


# In[11]:


#What is the total number and percentage of missing data in 2014 to 3 decimal places?
missing_values = data['Y2014'].isnull().sum()
total_values= len(data)
missing_percentage= (missing_values/total_values)*100
print('total number of missing data for 2014:', (missing_values))
print('percentage of missing data in 2014:', round((missing_percentage), 3), '%')


# In[12]:


#What is the total sum of Wine produced in 2015 and 2018 respectively?
Production_A = data.groupby('Item')['Y2015'].sum().loc['Wine']
Production_B = data.groupby('Item')['Y2018'].sum().loc['Wine']
print('The total sum of wine produced in 2015 and 2018 respectively is', (Production_A, Production_B))


# In[13]:


#Which year had the least correlation with ‘Element Code’?
correlations = data[['Element Code', 'Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']].corr()
least_correlated_year = correlations['Element Code'].abs().idxmin()
print('The year with the least correlation with "Element Code" is', (least_correlated_year))


# In[14]:


#Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the 7th lowest sum in 2017?
selected_columns = data[['Y2017', 'Area']]
grouped_data = selected_columns.groupby('Area')['Y2017'].sum().reset_index()
sorted_data = grouped_data.sort_values('Y2017')
seventh_lowest_area = sorted_data.iloc[6]['Area']
print('The area with the seventh lowest sum in 2017 is', (seventh_lowest_area))


# In[21]:


#Perform a groupby operation on ‘Element’.  What year has the highest sum of Stock Variation?
stock_variation_sum = data.groupby('Element')[['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']].sum()
sorted_data = stock_variation_sum.loc['Stock Variation']
print(sorted_data)


# In[22]:


#What is the mean and standard deviation across the whole dataset for the year 2017 to 2 decimal places?
details = data.describe()
Mean = details.loc['mean']
print(Mean)


# In[23]:


Standard_Deviation = details.loc['std']
print(Standard_Deviation)


# In[24]:


#Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the highest sum in 2017?
selected_columns = data[['Y2017', 'Area']]
grouped_data = selected_columns.groupby('Area')['Y2017'].sum()
area_with_the_highest_sum = grouped_data.idxmax()
print('The area with the highest sum is', (area_with_the_highest_sum))


# In[25]:


#What is the total number of unique countries in the dataset?
unique_countries = data['Area'].nunique()
print('There are', (unique_countries), 'unique countries')


# In[26]:


#What is the total Protein supply quantity in Madagascar in 2015?
madagascar_2015 = data[(data['Area'] == 'Madagascar') & (data['Element'] == 'Protein supply quantity (g/capita/day)')]['Y2015']
total_protein_supply = madagascar_2015.sum()
print('The total protein supply for Madagascar in 2015 is', round((total_protein_supply), 2))

