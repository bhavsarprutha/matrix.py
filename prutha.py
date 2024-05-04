def bubblesort():
    print("\n*******Bubble sort*********")
    c1 = int(input("Enter the student count:"))
    print("Enter the %i student first yesr percentage:" %(c1))
    mark = list(map(float,input().split(",")))
    n = len(mark)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if mark[j] > mark[j + 1]:
                temp=mark[j]
                mark[j]=mark[j + 1]
                mark[j+1]=temp
    print("sorted array is:bubble sort:")

    for i in range(len(mark)):
        print("%0.if" % mark[i])
    print("top 5 score:")
    print(mark[-5:n])
bubblesort()
def selection():
        print("\n*******selection sort********")
        c1 = int(input("Enter the student count:"))
        print("enter the %i student first yesr percentage:" % (c1))
        mark = list(map(float,input().split(",")))
        n=len(mark)
        for i in range(0,n-1):
            for j in range (i+1,n):
                if(mark[i]>mark[j]):
                    temp=mark[i]
                    mark[i]=mark[j]
                    print("sorted array is:selection sort:")
                    for i in range (len(mark)):
                        print("%0.if" %mark[i]),
                        print("top 5 score:")
                        print(mark[-5:n])
                                               
                        selection()
                        bubblesort()
