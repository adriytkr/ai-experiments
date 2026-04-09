from textblob import TextBlob

def compute_mood_and_subjectivity(text:str)->tuple[float,float]:
  blob=TextBlob(text)
  sentiment=blob.sentiment

  polarity=sentiment.polarity
  subjectivity=sentiment.subjectivity

  return polarity,subjectivity
