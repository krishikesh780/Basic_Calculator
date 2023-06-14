# Exception is an event which will couse program termintate
# try, except,,elese and finally-> Always Execute
def exceptional(x,y):
  try:
    a,b=x,y
    message=a/b
  except:
    message="When occurese-Exception handel"
  else:
      message="No Exception occure"
  return message
