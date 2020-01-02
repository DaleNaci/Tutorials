import requests, bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
elems = exampleSoup.select("#author") # elems is a list of Tag objects

type(elems) # <class 'list'>
len(elems) # 1
type(elems[0]) # <class 'bs4.element.Tag'>
str(elems[0]) # '<span id="author">Al Sweigart</span>'
elems[0].getText() # 'Al Sweigart'
elems[0].attrs # {'id': 'author'}


pElems = exampleSoup.select("p")

str(pElems[0]) # '<p>Download my <strong>Python</strong> book from <a
               # href="https://inventwithpython.com">my website</a>.</p>'
pElems[0].getText() # 'Download my Python book from my website'
str(pElems[1]) # '<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText() # 'Learn Python the easy way!'
str(pElems[2]) # '<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText() # 'By Al Sweigart'


spanElem = soup.select('span')[0]
str(spanElem) # '<span id="author">Al Sweigart</span>'
spanElem.get('id') # 'author'
spanElem.get('some_nonexistent_addr') == None # True
spanElems.attrs {'id': 'author'}
