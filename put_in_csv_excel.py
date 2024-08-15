import pandas as pd

f = open("reviews.txt", "r")
t = open("sentiments.txt", "r")
sentiment = t.read()
# load sentiment as list
sentiment = sentiment[1:-1].replace("'","").split(", ")


comments = [i.split(" :- ",2)+[j] for i,j in zip(f.readlines(),sentiment)]
# print(comments)

df = pd.DataFrame(comments, columns=["Trading app", "Source", "Comment", "Sentiment"])
# write to csv
df.to_csv("sentiments.csv", index=False)
#write to excel
df.to_excel("sentiments.xlsx", index=False)