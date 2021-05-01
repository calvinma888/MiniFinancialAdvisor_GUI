"""
Object Oriented Programming II: Final Project
Mini Financial Advisor

Yu chien Ma
"""


import tkinter as tk
import requests
import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import math
import pandas as pd
import numpy as np
from datetime import datetime
from textblob import TextBlob
import nltk
from newspaper import Article
import urllib
import requests
from bs4 import BeautifulSoup

    
app = tk.Tk()
title = tk.Label(app, text="Mini Financial Advisor", font='Times 30 bold',background='lightblue')
title.grid(row=0, column=0,columnspan=3,padx=0, pady=10)

app.geometry("900x550")
app.resizable(0, 0)
app.title("Mini Financial Advisor")
 
app.configure(background='lightblue')

errormessage = tk.Label(app, text="",font=("Times", 16),fg = 'red',background='lightblue')
errormessage.grid(row=10, column=1, pady=5, padx=5)


def scrapeandsentiment():
    """Scrapes top 50 Google search results for the stock and then analyzes the sentiment of the 50 articles, then updates the sentiment list"""

    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    query = stockticker
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"

    headers = {"user-agent": USER_AGENT}
    payload = { 'q' : query, 'start' : '0', 'num' : 50}

    resp = requests.get(URL, params = payload, headers=headers)

    global sentimentlist
    sentimentlist = []

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)
        for i in results:
            try:
                url = str(i['link'])
                article = Article(url)
                article.download()
                article.parse()
                article.nlp()
                text = article.summary
                obj = TextBlob(text)
                sentiment = obj.sentiment.polarity
                sentimentlist.append(sentiment)

            except:
                temp = str(i['link'])
                print(f"One URL: {temp} does not allow scraping")
                continue

    
def entered_stock(event):
    """Called when a ticker is entered, and then passes the stock ticker to requests to retrieve data from Yahoo Finance. It also updates all of the labels with values retrieved and gives a recommendation of buy, hold, or sell"""

    global stockticker
    stockticker = str(reponse.get())
    reponse.delete(0, tk.END)

    company["text"] = "Stock ticker: " + stockticker
    params = {"formatted": "true",
        "crumb": "AKV/cl0TOgz",
        "lang": "en-US",
        "region": "US",
        "modules": "defaultKeyStatistics,financialData,calendarEvents",
        "corsDomain": "finance.yahoo.com"}

    try:
        r = requests.get(f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{stockticker}", params=params)
        data = r.json()[u'quoteSummary']["result"][0]
        datadict = dict(data)
        errormessage["text"] = ""
    except:
        errormessage["text"] = "Please input a correct stock ticker!!"
    
    try:
        profitmargin["text"] = "Profit Margin: "+ str(datadict['defaultKeyStatistics']["profitMargins"]["fmt"])
    except:
        profitmargin["text"] = "Profit Margin: N/A"
    
    try:
        currentPrice["text"] = "Current Price: "+ str(datadict['financialData']["currentPrice"]["fmt"])
    except:
        currentPrice["text"] = "Current Price: N/A"
        
    try:
        earningsQuarterlyGrowth["text"] = "Earnings Quarter Growth: "+ str(datadict['defaultKeyStatistics']["earningsQuarterlyGrowth"]["fmt"])
    except:
        earningsQuarterlyGrowth["text"] = "Earnings Quarter Growth: N/A"
    
    try:
        priceToBook["text"] = "Price to Book: "+ str(datadict['defaultKeyStatistics']["priceToBook"]["fmt"])
    except:
        priceToBook["text"] = "Price to Book: N/A"
    
    try:
        enterpriseValue["text"] = "Enterprise Value: "+ str(datadict['defaultKeyStatistics']["enterpriseValue"]["fmt"])
    except:
        enterpriseValue["text"] = "Enterprise Value: N/A"
        
    try:
        returnOnAssets["text"] = "Return on Assets: "+ str(datadict['financialData']["returnOnAssets"]["fmt"])
    except:
        returnOnAssets["text"] = "Return on Assets: N/A"
        
    try:
        freeCashflow["text"] = "Free Cash Flow: "+ str(datadict['financialData']["freeCashflow"]["fmt"])
    except:
        freeCashflow["text"] = "Free Cash Flow: N/A"
        
    try:
        returnOnEquity["text"] = "Return on Equity: "+ str(datadict['financialData']["returnOnEquity"]["fmt"])
    except:
        returnOnEquity["text"] = "Return on Equity: N/A"
        
    try:
        debtToEquity["text"] = "Debt to Equity: "+ str(datadict['financialData']["debtToEquity"]["fmt"])
    except:
        debtToEquity["text"] = "Debt to Equity: N/A"
    
    try:
        revenuePerShare["text"] = "Revenue Per Share: "+ str(datadict['financialData']["revenuePerShare"]["fmt"])
    except:
        revenuePerShare["text"] = "Revenue Per Share: N/A"

    try:
        if datadict['financialData']["recommendationKey"] == "buy" or datadict['financialData']["recommendationKey"] == "strong buy":
            recommendationKey = tk.Label(app, text="  Recommendation for "+ stockticker +": Buy  ", font='Times 30 bold', fg="green",background='lightblue')
            recommendationKey.grid(row=11, column=1, columnspan=2, pady=5, padx=5)

        elif datadict['financialData']["recommendationKey"] == "hold":
            recommendationKey = tk.Label(app, text="   Recommendation for " + stockticker +": Hold   ", font='Times 30 bold', fg="orange",background='lightblue')
            recommendationKey.grid(row=11, column=1, columnspan=2, pady=5, padx=5)

        elif datadict['financialData']["recommendationKey"] == "underperform" or datadict['financialData']["recommendationKey"] == "sell":
            recommendationKey = tk.Label(app, text= "   Recommendation for " + stockticker+ ": Sell   ", font='Times 30 bold', fg="red",background='lightblue')
            recommendationKey.grid(row=11, column=1, columnspan=2, pady=5, padx=5)

    except:
        recommendationKey = tk.Label(app, text= "   Recommendation for " + stockticker+ ": N/A   ", font='Times 30 bold', fg="black",background='lightblue')
        recommendationKey.grid(row=11, column=1, columnspan=2, pady=5, padx=5)
        errormessage["text"] = "Please input a correct stock ticker!!"


def graph5years():
    """Graphs 5 years of historical data for the stock ticker entered"""

    try:
        if stockticker == "":
            raise NameError

        matplotlib.use('TKAgg')
        plt.rcParams['figure.dpi'] = 120
        plt.clf()
        window = tk.Toplevel(app)
        window.title("Stock Prices from the Last 5 Years")
        fig = plt.figure(1)

        canvas = FigureCanvasTkAgg(fig, master=window)
        plot_widget = canvas.get_tk_widget()
        matplotlib.use('TkAgg')

        data = yf.Ticker(stockticker)
        plt.plot(data.history(period="max")[-252*5:]["Close"], label='Daily', color = "green")
        plt.plot(data.history(period="max")[-252*5:]["Close"].rolling(window=20).mean(), label='20 days', color = "orange")
        plt.plot(data.history(period="max")[-252*5:]["Close"].rolling(window=50).mean(), label='50 days', color = "red")
        plt.plot(data.history(period="max")[-252*5:]["Close"].rolling(window=200).mean(), label='200 days', color = "navy")
        plt.title(stockticker+ " Stock Prices from the Last 5 Years")
        plt.xlabel("Date")
        plt.ylabel("Stock Price")
        plt.legend(loc='upper left',facecolor='white')

        plot_widget.grid(row=0, column=0)

    except:
        errormessage["text"] = "Please input a correct stock ticker!!"


def graph1year():
    """Graphs 1 year of historical data for the stock ticker entered"""

    try:
        if stockticker == "":
            raise NameError

        matplotlib.use('TKAgg')
        plt.rcParams['figure.dpi'] = 120
        plt.clf()
        window = tk.Toplevel(app)
        window.title("Stock Prices from the Last 1 Year")

        fig = plt.figure(1)
        canvas = FigureCanvasTkAgg(fig, master=window)
        plot_widget = canvas.get_tk_widget()
        matplotlib.use('TkAgg')

        data = yf.Ticker(stockticker)
        plt.plot(data.history(period="max")[-252:]["Close"], label='Daily', color = "green")
        plt.plot(data.history(period="max")[-252:]["Close"].rolling(window=20).mean(), label='20 days', color = "orange")
        plt.plot(data.history(period="max")[-252:]["Close"].rolling(window=50).mean(), label='50 days', color = "red")
        plt.title(stockticker+ " Stock Prices from the Last 1 Year")
        plt.xlabel("Date")
        plt.ylabel("Stock Price")
        plt.legend(loc='upper left',facecolor='white')
        plot_widget.grid(row=0, column=0)

    except:
        errormessage["text"] = "Please input a correct stock ticker!!"


def graph1month():
    """Graphs 1 month of historical data for the stock ticker entered"""

    try:
        if stockticker == "":
            raise NameError

        matplotlib.use('TKAgg')
        plt.rcParams['figure.dpi'] = 120
        plt.clf()
        window = tk.Toplevel(app)
        window.title("Stock Prices from the Last 1 Month")
        fig = plt.figure(1)
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        plot_widget = canvas.get_tk_widget()
        matplotlib.use('TkAgg')

        data = yf.Ticker(stockticker)
        plt.plot(data.history(period="max")[-30:]["Close"], label='Daily', color = "green")
        plt.title(stockticker+ " Stock Prices from the Last 1 Month")
        plt.legend(loc='upper left',facecolor='white')
        plt.xticks(rotation= 15)
        plt.ylabel("Stock Price")
        plot_widget.grid(row=0, column=0)

    except:
        errormessage["text"] = "Please input a correct stock ticker!!"

    
def updatesentiment():
    """Called when the Calculate Sentiment button is pressed. Displays sentiment score and also addes a comment of Positive, Negative, or Neutral to make it easier to interpret"""
    scrapeandsentiment()
    currentsentiment = sum(sentimentlist)/len(sentimentlist)
    if currentsentiment > 0.25:
        sentimentscore["text"] = str(sum(sentimentlist)/len(sentimentlist))[:9] + " (Positive)"
    elif currentsentiment < -0.25:
        sentimentscore["text"] = str(sum(sentimentlist)/len(sentimentlist))[:9] + " (Negative)"
    else:
        sentimentscore["text"] = str(sum(sentimentlist)/len(sentimentlist))[:9] + " (Neutral)"


b = tk.Button(app, text=" Graph 5 Year Historical Prices ", command=graph5years,font=("Times", 14),highlightbackground='lightblue')
b.grid(row=12, column=0,padx=0, pady=10)

b2 = tk.Button(app, text=" Graph 1 Year Historical Prices ", command=graph1year,font=("Times", 14),highlightbackground='lightblue')
b2.grid(row=11, column=0,padx=0, pady=10)

b3 = tk.Button(app, text=" Graph 1 Month Historical Prices ", command=graph1month,font=("Times", 14),highlightbackground='lightblue')
b3.grid(row=10, column=0,padx=0, pady=10)


lbl_reponse = tk.Label(app, text="Please enter a stock ticker symbol (ie. \"AAPL\" for Apple):", font=("Times", 16),background='lightblue')
lbl_reponse.grid(row=1, column=0, pady=5, padx=5)
 
reponse = tk.Entry(app,highlightbackground='lightblue')
reponse.grid(row=1, column=1, pady=5, padx=5)
reponse.bind("<Return>", entered_stock)

spacefiller = tk.Label(app, text="",background='lightblue')
spacefiller.grid(row=2, column=0, pady=5, padx=5)

spacefiller2 = tk.Label(app, text="",background='lightblue')
spacefiller2.grid(row=2, column=1, pady=5, padx=5)

spacefiller3 = tk.Label(app, text="",background='lightblue')
spacefiller3.grid(row=9, column=1, pady=5, padx=5)
 
company = tk.Label(app, text="Stock ticker: ", font='Times 18 bold',background='lightblue')
company.grid(row=3, column=0, pady=5, padx=5)

currentPrice = tk.Label(app, text="Current Price: ", font=("Times", 16),background='lightblue')
currentPrice.grid(row=4, column=0, pady=5, padx=5)

enterpriseValue = tk.Label(app, text="Enterprise Value: ", font=("Times", 16),background='lightblue')
enterpriseValue.grid(row=5, column=0, pady=5, padx=5)

priceToBook = tk.Label(app, text="Price to Book: ", font=("Times", 16),background='lightblue')
priceToBook.grid(row=6, column=0, pady=5, padx=5)

earningsQuarterlyGrowth = tk.Label(app, text="Earnings Quarterly Growth", font=("Times", 16),background='lightblue')
earningsQuarterlyGrowth.grid(row=7, column=0, pady=5, padx=5)

returnOnAssets = tk.Label(app, text="Return on Assets", font=("Times", 16),background='lightblue')
returnOnAssets.grid(row=8, column=0, pady=5, padx=5)

profitmargin = tk.Label(app, text="Profit Margin: ", font=("Times", 16),background='lightblue')
profitmargin.grid(row=4, column=1, pady=5, padx=5)

freeCashflow = tk.Label(app, text="Free Cash Flow: ", font=("Times", 16),background='lightblue')
freeCashflow.grid(row=5, column=1, pady=5, padx=5)

returnOnEquity = tk.Label(app, text="Return on Equity: ", font=("Times", 16),background='lightblue')
returnOnEquity.grid(row=6, column=1, pady=5, padx=5)

debtToEquity = tk.Label(app, text="Debt to Equity: ", font=("Times", 16),background='lightblue')
debtToEquity.grid(row=7, column=1, pady=5, padx=5)

revenuePerShare = tk.Label(app, text="Revenue per Share: ", font=("Times", 16),background='lightblue')
revenuePerShare.grid(row=8, column=1, pady=5, padx=5)

recommendationKey = tk.Label(app, text="Recommendation: ", font='Times 30 bold', fg="black",background='lightblue')
recommendationKey.grid(row=11, column=1, pady=5, padx=5)
 
spacer = tk.Label(app, text="", font=("Times", 16),background='lightblue')
spacer.grid(row=4, column=2, pady=5, padx=5)

sentiment = tk.Label(app, text="Sentiment: ", font='Times 18 bold',background='lightblue')
sentiment.grid(row=5, column=2, pady=5, padx=5)

sentimentscore = tk.Label(app, text="", font=("Times", 16),background='lightblue')
sentimentscore.grid(row=6, column=2, pady=5, padx=5)

b4 = tk.Button(app, text=" Calculate Sentiment ", command=updatesentiment,font=("Times", 14),highlightbackground='lightblue')
b4.grid(row=7, column=2, pady=5, padx=5)

spacer5 = tk.Label(app, text="", font=("Times", 16),background='lightblue')
spacer5.grid(row=8, column=2, pady=5, padx=5)


def close_window():
  app.quit()
  print ("Thank you for using Mini Financial Advisor!")
  

app.protocol("WM_DELETE_WINDOW", close_window)

app.mainloop()

    