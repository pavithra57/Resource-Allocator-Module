def get_costs(instances,hours,cpus,price):
    finall=[]
    for key in instances:
        res = key
        def findservers_cpus(a):
                l=xl=xl2=xl4=xl8=xl10=0;
                while (a < 0):
                    break
                
                while (a > 0):
                        while (a >= 32):
                            a = a - 32;
                            xl10+=1
                        while (a >= 16):
                            a = a - 16;
                            xl8+=1
                        while (a >= 8):
                            a = a - 8;
                            xl4+=1
                        while (a >= 4):
                            a = a - 4;
                            xl2+=1
                        if(res=='us-east'):
                            while (a >= 2):
                                a = a - 2;
                                xl+=1
                        while (a >= 1):
                            a = a - 1;
                            l+=1
                servers={'large':l,'xlarge':xl,'2xlarge':xl2,'4xlarge':xl4,'8xlarge':xl8,'10xlarge':xl10}
                cost={'large':l*hours*instances[res]["large"],'xlarge':xl*hours*instances[res]["xlarge"],'2xlarge':xl2*hours*instances[res]["2xlarge"],'4xlarge':xl4*hours*instances[res]["4xlarge"],'8xlarge':xl8*hours*instances[res]["8xlarge"],'10xlarge':xl10*hours*instances[res]["10xlarge"]};
                total_cost=cost['large']+cost['xlarge']+cost['2xlarge']+cost['4xlarge']+cost['8xlarge']+cost['10xlarge']
                server=[]
                d={}
                server=[]
                for key in servers:
                    if(servers[key]>0):
                        d[key]=servers[key]
                server.append(d)
                Final={"region":res,"Total_cost":('$'+('%.2f'%total_cost)),"Servers":server}
                return(Final)
        def findservers_price(price):
            l=xl=xl2=xl4=xl8=xl10=0;
            temp=price;
            while (price < 0):
                break
            while (price>(hours*instances[res]["large"])):
                price=price-(hours*instances[res]["large"])
                l+=1
            price=temp
            if(res=='us-east'):
                while (price>instances[res]["xlarge"]):
                    price=price
                    price=price-(hours*instances[res]["xlarge"])
                    xl+=1
            price=temp
            while (price>instances[res]["2xlarge"]):
                price=price-(hours*instances[res]["2xlarge"])
                xl2+=1
            price=temp
            while (price>instances[res]["4xlarge"]):
                price=price-(hours*instances[res]["4xlarge"])
                xl4+=1
            price=temp
            while (price>instances[res]["8xlarge"]):
                price=price-(hours*instances[res]["8xlarge"])
                xl8+=1
            price=temp
            while (price>instances[res]["10xlarge"]):
                price=price-(hours*instances[res]["10xlarge"])
                xl10+=1
            dictt={"large":l,"xlarge":xl,"2xlarge":xl2,"4xlarge":xl4,"8xlarge":xl8,"10xlarge":xl10}
            Keymax = max(dictt, key=dictt.get)
            total_cost=hours*dictt[Keymax]*instances[res][Keymax]
            Final={"region":res,"Total_cost":('$'+('%.2f'%total_cost)),"Servers":{Keymax:dictt[Keymax]}}
            return(Final)
        if(((cpus>0) and (hours>0)) and (price==0)):
            dicti={}
            dicti=findservers_cpus(cpus);
        elif(((price>0) and (hours>0)) and (cpus==0)):
            dicti={}
            dicti=findservers_price(price)
        elif(((cpus>0) and (hours>0)) and (price > 0)):
            print("Finding the Servers for the given amount and number of CPUs is under progress")
            dicti={}
            dicti=findservers_cpus(cpus);
        d1={}
        for keyy in dicti:
            d1[keyy]=dicti[keyy]
        finall.append(d1)
    print(finall)
    
instances ={
"us-east": {
"large": 0.12,
"xlarge": 0.23,
"2xlarge": 0.45,
"4xlarge": 0.774,
"8xlarge": 1.4,
"10xlarge": 2.82
},

"us-west": {
"large": 0.14,
"xlarge":0.00,
"2xlarge": 0.413,
"4xlarge": 0.89,
"8xlarge": 1.3,
"10xlarge": 2.97
},
}
hours=int(input("Hours required: "))
cpus=int(input("CPUs required: "))
prize=float(input("Budget: "))
get_costs(instances,hours,cpus,prize);
