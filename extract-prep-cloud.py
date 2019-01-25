from urllib.request import urlopen;
from bs4 import BeautifulSoup;
import pandas as pd;
from wordcloud import WordCloud, STOPWORDS ;
import matplotlib.pyplot as plt ;
from joblib import Parallel, delayed;
import random;
import time;
import threading;
import os;


product_id = "B07HCXQZ4P";
reviews = [];

def ScrapePage(pagenum):
    reviewpageurl = url +str(pagenum);
    exceptionstatus = True;
    scrape_attempt = 0;
    while exceptionstatus and scrape_attempt < 3:
        try:
            print("\nExtracting reviews for :"+str(pagenum)+", ATTEMPT : "+str(scrape_attempt));
            html = urlopen(reviewpageurl);
            soup = BeautifulSoup(html,'lxml');
            review_text = soup.find_all("span",class_="a-size-base review-text");
            for review in review_text:
                reviews.append(review.get_text());
            df = pd.DataFrame(reviews);
            if not os.path.isfile(r'\review_'+product_id+'.csv'):
               df.to_csv(r'\review_'+product_id+'.csv', header=False,index=False)
            else: # else it exists so append without writing the header
                with open(r'\review_'+product_id+'.csv', 'a') as f:
                    df.to_csv(f, header=False,index=False)
            exceptionstatus = False;
        except Exception as e:
            print('\n Exception at : '+str(pagenum)+'-'+str(e));
            scrape_attempt+=1;
    sleeptime = random.randint(1,3); 
    print('\n'+ str(threading.current_thread())+'Sleeping for : '+str(sleeptime));
    time.sleep(sleeptime);
    
def ExtractWords(val):
    cw= ' ';
    print('val :'+val);
     # typecaste each val to string 
    val = str(val).lower(); 
  
    # split the value 
    tokens = val.split(); 
          
    for words in tokens:
        cw = cw + words + ' ';
    print('cw after :'+cw);
    return str(cw);


#------------------Getting the number of pages in review

url = "https://www.amazon.in/product-reviews/"+product_id+"/ref=cm_cr_getr_d_paging_btm_2?showViewpoints=1&pageNumber=";
html = urlopen(url+"1");

soup = BeautifulSoup(html,'lxml');
page_buttons = soup.find_all("li",class_="page-button");
pagecount = int(page_buttons[len(page_buttons)-1].get_text().replace(",",""));

#-----------------Identifying the number of threads needed to scrape the reviews

if pagecount < 10:
    threadcount = pagecount;
else:
    threadcount = pagecount / 10;

threadcount = int(threadcount);
threadcount = 8;
print('\nThreads created :'+str(threadcount));
#-----------------Scraping the reviews multi threaded

Parallel(n_jobs=threadcount,prefer="threads")(delayed(ScrapePage)(i) for i in range(1,pagecount));    

print('\n Scraping complete!');
#-----------------Saving the scraped reviews in to a csv through dataframe

#df = pd.DataFrame(reviews);
#df.to_csv(r'C:\Users\Aadhithyan_Balaji\Desktop\review_'+product_id+'.csv');

df = pd.read_csv(r"c:\users\aadhithyan_balaji\desktop\review_"+product_id+".csv", encoding ="latin-1",usecols=[1])

print(df);

comment_words = ' ';
stopwords = set(STOPWORDS) 
# iterate through the csv file
comment_words = comment_words + str(Parallel(n_jobs=threadcount,prefer="threads")(delayed(ExtractWords)(frame) for frame in df));    
     
print('\nExtracted words from the review!\nPreparing the word cloud...')  ;
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 

print('\nPlotting word cloud')  ;
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 
