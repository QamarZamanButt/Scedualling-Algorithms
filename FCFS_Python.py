n=input("Enter Number of Processes: ")
name={}
arr={}
bur={}
wt={}
tt={}
avg_waiting=0
avg_turnaround=0
total_time=0

def sort(a,b,c,size):
    for i in range (size-1):
        for j in range (size-i-1):
            if(a[j] >a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

                temp=b[j]
                b[j]=b[j+1]
                b[j+1]=temp

                temp=c[j]
                c[j]=c[j+1]
                c[j+1]=temp                
                

print("\n")
for i in range(n):
    name[i]=raw_input("Enter Name of Process:  ")
    arr[i]=int(input("Enter Arrival Time of Process: "))
    bur[i]=int(input("Enter Burst Time of Process: "))
    print("\n")

sort(arr,name,bur,n)


    
wt[0]=0

for i in range(n):
    
    if arr[i]>total_time:
            print("CPU is Idle")
            new=arr[i]-total_time
            import time
            time.sleep(new)
            total_time += new

    start=total_time
    print name[i]," is Executing"
    import time
    time.sleep(bur[i])
    #t_time = tt[i] + arr[i]
    total_time=total_time+bur[i]
    End=total_time
    print name[i]," Executed at ",End
    wt[i]=start-arr[i]
    tt[i]=End-arr[i]
    avg_waiting += start-arr[i]
    avg_turnaround += End-arr[i]
    
import time
time.sleep(3)

import os
os.system('cls')

print ("Process Name\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time |")
print ("--------------------------------------------------------------------------------|")
for i in range (n):
    print name[i],"\t\t",arr[i],"\t\t",bur[i],"\t\t",wt[i],"\t\t",tt[i],"\t\t|"
print ("________________________________________________________________________________|")
    
avg_waiting=avg_waiting/n
avg_turnaround=avg_turnaround/n

print "\n\nAverage Waiting Time::  ",avg_waiting
print "\nAverage Turnaround Time::  ",avg_turnaround,"\n\n"
