import re

text = "Rated 4.3 out of 5 stars based on 265 reviews."
textrevised = re.findall(r"\d\.\d", text)
ftext = textrevised[0]
floattext = float(textrevised)
print(type(floattext))