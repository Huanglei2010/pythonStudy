import os
import sys
def text_create(name, msg):
    desktop_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
    full_path = desktop_path +'\\'+ name + '.py'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
if __name__ == "__main__":
    print (os.path.realpath(sys.argv[0]))
    print (os.path.split(os.path.realpath(sys.argv[0])))
    print (os.path.split(os.path.realpath(sys.argv[0]))[0])
    print(os.path.split("a/b/c/d/"))
    print(os.path.split("a/b/c/d"))
    for i in range(1,11):
        name='38_'+str(i)
        msg="#encoding: UTF-8"
        text_create(name,msg)

'''http://www.cnblogs.com/goodright/p/5886188.html'''