def readFile():
    i = 0
    occupations = {}
    f = open("occupations.csv", 'rU')
    stuff = f.read();
    lst = stuff.split('\n')
    lst = lst[1:-1]
    counter = 0 

    while i < len(lst):
        item = lst[i]
        pos = item.find(',')
        title = item[0:pos]
        
        percentage = item[pos+1:]
        print item
        print pos
        print percentage
        
 #       percentage= float(percentage)
        print percentage
  #     occupations[title] = [counter, counter+percentage]
        i += 1
 #       counter+= percentage

    return occupations 
        

        
        
        
        
        

    

    
    
