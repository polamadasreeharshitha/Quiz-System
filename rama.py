c=0
while(c<5):
        line_number = int(input('Enter the line number: '))
        with open('question') as f:
            i = 1
            for line in f:
                if i == line_number:
                    break
                i += 1
        print(line,end="")
        x=input()
        count=0
        with open('answer') as f1:
            i = 1
            for line1 in f1:
                if i == line_number:
                    break
                i += 1
        line2=line1[:len(line1)-1]
        if(x==line2):
                if(c<4):
                        print("Congratulations! Go for next one")
                c+=1
        else:
                while(x!=line2 and count<2):
                        count=count+1
                        print("Try Again!!")
                        x=input()
                        if(x==line2):
                           if(c<4):
                                  print("Congratulations! Go for next one")
                           c+=1
                           continue
        if(x!=line2 and count==2):
                print("Better Luck Next Time!!")
                break

if(c>=5):
       print("U Won!!")                       

