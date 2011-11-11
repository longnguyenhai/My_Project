import sys
fo = open('/etc/passwd','r')

def break_word(suff):
    word=suff.split(':')
    return word

while True:
    line = fo.readline()
    if len(line) == 0:
        break
    word= break_word(line)
    if len(sys.argv) <2:
        print '%s --> %s'%(word[0], word[-1])
    else:
        if sys.argv[1] == word[0]:
            print '%s --> %s'%(word[0], word[-1])
fo.close    ()
       

    
#######
