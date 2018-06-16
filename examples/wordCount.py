wc = """Speaking at a conference in Israel, Mr Giuliani said Mr Trump's tough stance had forced Pyongyang's hand. 
Mr Trump called off the summit in May, accusing North Korea of "tremendous anger and open hostility".
But plans for the 12 June bilateral in Singapore were revived after a conciliatory response from Pyongyang.
Mr Giuliani was speaking at an investment conference in Israel when he made the remark."""

print(wc)
words = wc.split()

print(len(words))

d= {}.fromkeys(words, 0)
for w in words:
    d[w] +=1

print(d)