# amazon-review-wordcloud
A python script to scrape Amazon reviews and generate wordcloud based on Product ID

<b> Introduction </b>

The most sought after products on Amazon have pages and pages of their reviews. Any potential buyer cannot be expected to go through 1500+ pages of reviews to understand what the previous buyers/ owners of the product had to say. Hence this project.

The reason why I selected Python for this was purely out of my interest to explore Python. 

This project consists of two parts:

- Scraping Amazon review pages with <b>urlopen</b> and extract Review information using <b>BeautifulSoup</b>
- Preparing Word cloud out of it using <b>Pandas</b> and <b>WordCloud</b>
- Plotting the same with <b> MatPlotLib </b>

<b> Packages Used </b>

- urllib.request 
- bs4
- pandas
- wordcloud
- matplotlib.pyplot
- joblib
- random
- time
- threading
- os

<b> Part I - Web Scraping </b>

Defined a Python function to perform the scraping from <b> one </b> page of Amazon review. Then implemented a Multithreaded approach to simultaneously connect to different pages of the Product reviews and perform scraping parallely. Also, introduced a Thread.Sleep to prevent DDoS-like requests firing

<b> Part II - Preparing & Plotting Word Cloud </b>

This part is completely on Python. I simply made use of the <b> WordCloud </b> package and it took care of the rest. It included support for STOPWORDS - words like "a","the","that","we",etc which should not contribute to the wordcloud.

The prepared wordcloud is plotted using MatPlotLib which produces a beautiful Word cloud!

