from google_play_scraper import Sort, reviews
app_id=["com.zerodha.kite3","com.nextbillion.groww","in.upstox.app","com.paytmmoney","com.dhan.live","com.mosl.mobile","com.msf.angelmobile","com.sharekhan.androidsharemobile","com.msf.emt.mobile","com.hsl.investright"]
app=["Zerodha Kite","Groww","Upstox","Paytm Money","Dhani Stocks","Motilal Oswal","Angel Broking","Sharekhan","Nuvama","HDFC Securities"]
for i,j in enumerate(app_id):
    result, continuation_token = reviews(
        j,
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.MOST_RELEVANT, # defaults to Sort.NEWEST
        count=600
    )
    k = 0
    # write only the comments part of each dictionary in reviews.txt
    with open('reviews.txt', 'a') as f:
        for review in result:
            
            try:
                if k+1<=300:
                    k+=1
                    f.write(app[i]+" :- "+"Play"+" :- "+review['content'])
                    f.write('\n')
                else:
                    k+=1
                    f.write(app[i]+" :- "+"Reddit"+" :- "+review['content'])
                    f.write('\n')
            except:
                continue
