#Write a functin for printing elements

def fibonicis(number):
    result =1;
    tempResult=0;
    value=0;
    finalResult=[]
    if number==0:
        print("Number is less than 0")
        #return value;
    elif number>0:
        while number>result:
            result=result+tempResult
            tempResult=value
            value=result
            finalResult.append(result)

        return finalResult


        #print("finalResult : " ,finalResult)

print("**** Function definatino Example **********")
result =fibonicis(100)
print(result)
