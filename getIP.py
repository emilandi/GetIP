from requests import get

public = get('https://api.ipify.org').text

print ('Public IP Address: ' +  public)
