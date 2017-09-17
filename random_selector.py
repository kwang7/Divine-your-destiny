occupations = {}

def readFile():
    i = 0
    f = open("occupations.csv", 'rU')
    stuff = f.read();
    lst = stuff.split('\n')
    lst = lst[1:-1]
    counter = 0 
    print lst
    print "\n"
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
           
        percent = float(percent)
        occupations[title] = [counter, counter+percent]
        i +=1
        counter += percent
        
    return occupations
  
        
readFile()
print "\n"
for keys,values in occupations.items():
    print keys
    print values

    

    
    
