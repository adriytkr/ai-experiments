def process_mood(mood:float)->tuple[str,str]:
  if mood<=-0.6:
    return 'Very Negative','#E53935'
  elif mood<=-0.2:
    return 'Negative','#EF9A9A'
  elif mood<=0.2:
    return 'Neutral','#F5F5F5'
  elif mood<=0.6:
    return 'Positive','#A5D6A7'
  else:
    return 'Very Positive','#43A047'

def process_subjectivity(subjectivity:float)->tuple[str,str]:
  if subjectivity<=0.2:
    return 'Very Objective','#CFD8DC'
  elif subjectivity<=0.4:
    return 'Objective','#B0BEC5'
  elif subjectivity<=0.6:
    return 'Neutral','#F5F5F5'
  elif subjectivity<=0.8:
    return 'Subjective','#FFCC80'
  else:
    return 'Very Subjective','#FFB74D'
