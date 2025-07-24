text = "X-DSPAM-Confidence:    0.8475"
extract = text.find('0.8475')
#print(extract)
print(float(text[extract:]))