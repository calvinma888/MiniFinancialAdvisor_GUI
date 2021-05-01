# Mini Financial Advisor

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
I chose to make this application because I retrieved many financial datasets from Yahoo Finance and Wharton Research Data Services (WRDS), and both of these financial databases download the data for each stock separately, and I spent a lot of time cleaning and reorganizing the datasets before I could even use it. Their databases are also very cluttered and filled with information that I do not need, and I had to keep scrolling and clicking around to find what I was looking for, which wasted a lot of time.
Therefore, I created the Mini Financial Advisor. The purpose of Mini Financial Advisor is to provide a fast, concise, and informative summary of any stock, and then the Mini Financial Advisor will give a recommendation of whether to buy, hold, or sell the stock. It retrieves data from Yahoo Finance, and can give 10 important financial statistics about the stock including:
1) Current Price, which is the current price that each share is trading for,
2) Enterprise Value, which measures the company’s total value,
3) Price to Book Ratio, which is the stock price divided by its book value per share,
which can be useful in finding undervalued stocks,
4) Earnings Quarterly Growth, which is the growth of sales in one quarter when
compared with another quarter,
5) Return on Assets, which measures how profitable a company is compared to its total
assets,
6) Profit Margin, which is the revenue after subtracting all the costs of business,
7) Free Cash Flow, which is the cash leftover after paying for operational costs,
8) Return on Equity, which is the profitability of a business in relation to its equity,
especially used to compare companies in the same industry,
3
9) Debt to Equity, which measures a company’s financial leverage because it measures how much a company is financing its operations through debt, and
10) Revenue per Share, which is the total revenue earned per share over the quarter.
After the financial data have been displayed, the Mini Financial Advisor will also give a recommendation as to buy, hold, or sell the particular stock. Once a stock ticker has been entered, the application can also plot historical price data directly from the application. Users can select 1 month of historical data, 1 year of historical data, or 5 years of historical data to plot, and a new window with the graph plotted.
Additionally, users can also calculate the sentiment of a particular company using the “Calculate Sentiment” button on the right side. This will calculate the average sentiment of the top 50 Google search results. This will give a sentiment score, which will be modified by a comment stating positive (>0.25), neutral (-0.25 to 0.25), or negative (-0.25). If the news about a particular company is overwhelmingly positive or negative, then investors should reconsider any financial strategies and take into account the market sentiment before selling or buying the stock.


### Built With

* []()Python


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

This is a list of packages that need to be installed before the notebook can be run.
* sklearn
* quandl
* yFinance
* BeautifulSoup
* Datetime
* FigureCanvasTkAgg
* NLK
* Requests
* TextBlob
* Tkinter
* pandas
* numpy
* matplotlib
* scipy


### Installation

Clone the repo: https://github.com/calvinma888/MiniFinancialAdvisor_GUI.git
   

<!-- USAGE EXAMPLES -->
## Usage

Run with Jupyter Notebook


<!-- CONTRIBUTING -->
## Contributing

Calvin (Yu chien) Ma

