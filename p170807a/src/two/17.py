
# 终极版作用域

name = "lzl"
n=2

def f1():
    global n
    n=n+1
    print(n)
f1()

li=[lambda :x for x in range(10)]
print(type(li))
print(li)
print(type(li[0]))
print(li[0])
print(li[0]())
for x in li:
    print(x())

SOLR_URL='http://solr.org'
def tt():
    global SOLR_URL
    SOLR_URL=SOLR_URL+'#aa'


tt()
print( SOLR_URL)


