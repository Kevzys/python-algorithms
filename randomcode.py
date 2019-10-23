import requests

people = {
            "Meta Data": {
                "1. Information": "Daily Prices (open, high, low, close) and Volumes",
                "2. Symbol": "AAPL",
                "3. Last Refreshed": "2019-09-27",
                "4. Output Size": "Compact",
                "5. Time Zone": "US/Eastern"
            },
            "Time Series (Daily)": {
                "2019-09-27": {
                    "1. open": "220.5400",
                    "2. high": "220.9600",
                    "3. low": "217.2800",
                    "4. close": "218.8200",
                    "5. volume": "25352000"
                },
                "2019-09-26": {
                    "1. open": "220.0000",
                    "2. high": "220.9400",
                    "3. low": "218.8300",
                    "4. close": "219.8900",
                    "5. volume": "18833500"
                }
            }
        }



count = 0
count2 = 0
count3 = 0
tmp = ''

for key1, value1 in people.items():

    print("\nPerson ID: ", key1)
    if count == 1:
        for  key2, value2 in value1.items():
            print("---------")
            print(key2)
            print("---------")
            for key3, value3 in value2.items():
                count2 += 1
                if count2 == 1:
                    print("open: " + value3)
                if count2 == 4:
                    print("close: " + value3)
                if count2 == 5:
                    count2 = 0

                #print(key3)
                #print(value3) # VALUE3 FINDS THE PRICES, now need to compare the last 2 values
                """
                if count2==0:
                    temp = value3
                else:
                    if value3 > tmp:
                        print("price went up")
                count2 += 1
                """
                #if count == 1:
                #    break
    count+=1
