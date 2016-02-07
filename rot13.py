def rot13(text):
	rt=""
	for c in text:
	    temp=ord(c)
	    if (temp >= ord('A')) and (temp <= ord('Z')):
	    	temp = ((temp - ord('A') + 13) % 26 + ord('A'))

	    if (temp >= ord('a')) and (temp <= ord('z')):
	    	temp = ((temp - ord('a') + 13) % 26 + ord('a'))	  

	    rt=rt+ chr(temp) 
	return rt    	
