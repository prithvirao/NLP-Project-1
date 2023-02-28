# NLP-Project-1

Here we present demo code for our real-time event detection and summarization project. 
The code gets 'm' number of tweets in real time from past 'n' number of dates.
The values of 'm' and 'n' can be modified as per you like

There is a list 'keywords' where you specify the keyword or keywords you want to use to get updates on.
In this demo the 'keywords' has been set to 'earthquake'

# Setting up the environment

The dependencies have been specified in the requirements file. 
You can simply run 
```diff
**pip install -r requirementss.txt**
```

They are also specified in the ipynb file for ease so that you can directly start using the ipynb file. When you open the ipynb file, you will see an option on the top to open with 
```diff
**google collab** 
```
as well.



# Working of the code

The code gets data in real-time from twitter. We are using Twitter API for the same. If you have the Twitter API credentials, you can set up your credentials as well


# Event Analysis 
We are performed event-analysis combining keyword-based filtering and geographical data. Instead of using the metadata of the twitter user to find the location. We are using Spacy and Nlp library to extract the location information directly from the tweet body. We are doing this in order to produce more relevant summaries according to the places where the events are actually happening.

# Summarization
For summarization, we are using a pretrained machine learning-based model 'T-5'. We have also experimented with 'Bert' but we observed better results from the 'T-5' model.
The code will produce summaries clustered on the basis of the locations where the event occured for each day. 

# Reproducable Results
This sample code has been set to obtain 100 tweets per day for keyword 'earthquake'. The code works in real-time, so when the code was run, the no of days was set to 5, thus summarization started from 2023-02-22. 
To obtain the same results as shown in the jupyter notebook,   
```diff
**please change the value of no of days with respect to the current date**   
```
so that the results start from 2023-02-22. In the jupyter notebook we have also highlighted the part from where you can change the no of days.
