print ("Εισάγεται διαδοχικά την αρχή και το τελος των διαστημάτων σε διαφορετικα κελιά το καθενα(Για τερματισμο εισαγεται το 0 στη λιστα):")
print("Αν θελετε το 0 για αρχη διαστηματος αντικαταστηστε το με 1 και προσθεστε μια μοναδα στο τελος του διαστηματος για να αποφυγουμε τον τερματισμο της λιστας!!")
List1 = []
while (True):
    item = int(input())
    List1.append(item)
    if (item==0):
        break
print (List1)
def sumIntervals(alist):
    S=0
    i=0
    while(alist[i]!=0):
        S=S+(alist[i+1]-alist[i])
        i=i+2
        z=i
        while(z>0):
            if(alist[i]>=alist[z-1]):
                z=z-2
            elif(alist[i+1]<alist[z-2]):
                z=z-2
            elif(alist[i+1]<alist[z-1] and alist[i]>alist[z-2]):
                S = S - (alist[i + 1] - alist[i])
                z=z-2
            elif(alist[i+1]>alist[z-1] and alist[i]>alist[z-2]):
                S=S -(alist[z-1]-alist[i])
                z=z-2
            elif(alist[i+1]<alist[z-1] and alist[i]<alist[z-2]):
                S = S - (alist[i+ 1] - alist[z-2])
                z=z-2
            elif (alist[i+1]>alist[z-1] and alist[i]<alist[z-2]):
                S= S - (alist[z-1] - alist[z-2])
                z=z-2

    print (S)

sumIntervals(List1)
