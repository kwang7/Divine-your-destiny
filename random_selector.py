def readFile():
    i = 0
    occupations = {}
    f = open("occupations.csv", 'rU')
    stuff = f.read();
    lst = stuff.split('\n')
    lst = lst[1:-1]
    counter = 0 

    while i < len(lst) :
        item = lst[i]
        
        if item[0] == '"' :
            item = item[1:]
            pos = item.find('"')
            title = item[0:pos]
            percent = item[pos+2:]
            print "title: " + title
            print "percent: " + percent
            
        else:
           pos = item.find(',')
           title = item[0:pos]
           percent = item[pos+1:]
           print "title: " + title
           print "percent: " + percent
        i +=1
  
        
readFile()


    

    
    
