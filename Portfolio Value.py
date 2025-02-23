#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas yfinance


# In[4]:


import yfinance as yf
import pandas as pd


# In[22]:


portfolio = {"AAPL": 10, "MSFT": 5, "GOOGL": 3, "TSLA": 5}


# In[23]:


portfolio_data = []
for stock, shares in portfolio.items():
    price = yf.Ticker(stock).history(period="1d")["Close"].iloc[-1]
    portfolio_data.append({"Stock": stock, "Shares": shares, "Price": price, "Value": shares * price})


# In[ ]:


df = pd.DataFrame(portfolio_data)
print(df)
print("Total Portfolio Value: $", df["Value"].sum())


# In[24]:


df = pd.DataFrame(portfolio_data)
print(df)
print("Total Portfolio Value: $", df["Value"].sum())


# In[ ]:





# In[ ]:





# In[ ]:




