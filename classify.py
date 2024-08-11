from time import sleep
import google.generativeai as genai
import api

genai.configure(api_key=api.API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
promt = "I will give you a comment and you have to classify it as positive or negative or neutral. If the comment contains any explicit words, classify it as explicit. Only give any of the 4 words as output: positive, negative, neutral, explicit. Use this same promt for everything I send here after. The comment is :- "

f = open("reviews.txt", "r")

comments = [i.split(" :- ",2) for i in f.readlines()]
temp = model.generate_content(promt+comments[0][2]).text.strip()
print(temp)



for i in range(len(comments)):
    sleep(3)
    temp = model.generate_content(comments[i][2]).text.strip()
    print(temp)
    # with open('classify.txt', 'a') as f:
    #     f.write(temp)
    #     f.write('\n')
    from time import sleep
import google.generativeai as genai
import api

genai.configure(api_key=api.API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
promt = "I will give you a comment and you have to classify it as positive or negative or neutral. If the comment contains any explicit words, classify it as explicit. Only give any of the 4 words as output: positive, negative, neutral, explicit. Use this same promt for everything I send here after. The comment is :- "

f = open("reviews.txt", "r")

comments = [i.split(" :- ",2) for i in f.readlines()]
temp = model.generate_content(promt+comments[0][2]).text.strip()
print(temp)



for i in range(len(comments)):
    sleep(3)
    temp = model.generate_content(comments[i][2]).text.strip()
    print(temp)
    # with open('classify.txt', 'a') as f:
    #     f.write(temp)
    #     f.write('\n')
    