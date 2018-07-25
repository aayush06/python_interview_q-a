'''
    Atbash is a simple substitution cipher originally for the Hebrew alphabet, but possible with any known alphabet.

    Original:   abcdefghijklmnopqrstuvwxyz  
    Substitute: ZYXWVUTSRQPONMLKJIHGFEDCBA
    So you would substitute "a" in your input text with "Z" in your output text, "b" with "Y", "c" with "X" and so forth.

    A few English words also 'Atbash' into other English words: "irk"="rip", "low"="old", "hob"="sly", "hold"="slow", "holy"="slob", "horn"="slim", "glow"="told", "grog"="tilt" and "zoo"="all". Some other English words Atbash into their own reverses, e.g., "wizard" = "draziw."
'''

d = {
     'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r',
     'j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'
    }

xx = ''
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in d:
        xx += d[i].upper()

