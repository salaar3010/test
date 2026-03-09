'''
############################
# LAB 1 — INTRODUCTION TO R
############################

c(100,200,300)
pi
5^3
2+(3*5)
2+3*5
(2+3)*5
log(92.13)
1:15
1/0
sqrt(-1)

a=-10
a

x=as.character(3.46)
x

paste("First","Second","Third")
paste("First","Second","Third",sep=":")
paste("First","Second","Third",sep=".")

m=c(1,2,3,4)
n=c(1,2,3,4)

m+n
6*m
m/3
2*n+1
m/n

x=c(4,6,8,9)
y=c("YES","NO","YES","YES")
z=c("ims","uds","neni","niti")

df=data.frame(x,y,z)
df

y=c(TRUE,FALSE,FALSE,TRUE)
df=data.frame(x,y,z)
df

mtcars
mtcars[23,4]
mtcars["Fiat 128","cyl"]

head(mtcars)
tail(mtcars)
head(mtcars,n=7)
head(mtcars,n=12)


############################
# LAB 2 — DATA VISUALIZATION
############################

empid=c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
empid

age=c(30,37,45,32,50,60,35,32,34,43,50,60,78,51,55)
age

sex=c(0,1,0,1,1,0,1,1,0,0,1,0,1,1,0)
sex

status=c(1,1,2,2,1,1,1,2,2,1,2,1,2,1,2)
status

empinfo=data.frame(empid,sex,age,status)
empinfo

empinfo$sex=factor(empinfo$sex,labels=c("male","female"))
empinfo$status=factor(empinfo$status,labels=c("staff","faculty"))

summary(empid)
summary(status)
summary(empinfo)

table1=table(empinfo$status)
table1

table2=table(empinfo$sex,empinfo$status)
table2

plot(empinfo$age,type="l",main="age of subject",xlab="empid",ylab="age in years",col="red")

plot(empinfo$status,type="l",main="status of subjects",xlab="empid",ylab="status",col="blue")

pie(table2)
pie(table1)

barplot(table2,beside=T,xlim=c(1,15),ylim=c(0,5),col=c("pink","orange"))
legend("topright",legend=rownames(table2),fill=c("pink","orange"),bty="n")

boxplot(empinfo$age-empinfo$status,col=c("pink","orange"))

hist(empinfo$age)

mydata=read.csv("diabetes.csv")
mydata

data1=read.csv(file.choose())
summary(data1)

table3=table(data1$Previous.Scores,data1$Sample.Question.Papers.Practiced)
table3

table4=table(data1$Hours.Studied,data1$Performance.Index)
plot(table4)


#############################################
# LAB 4 — HYPOTHESIS TESTING & CONFIDENCE
#############################################

xbar=14.6
mu0=15.4
sigma=2.5
n=35

z=(xbar-mu0)/(sigma/sqrt(n))

alpha=0.05
zalphahalf=qnorm(1-(alpha/2))
c(-zalphahalf,zalphahalf)

pval=2*pnorm(z)

if(pval>alpha){
print("Accept null hypothesis")
}else{
print("Reject null hypothesis")
}

# Problem 2

n=640
Sampleprop=63/n
Populationprop=0.1726
Q=1-Populationprop

z=(Sampleprop-Populationprop)/sqrt(Populationprop*Q/n)

E=qnorm(.975)
c(-E,E)

Sampleprop+c(-E,E)*sqrt(Populationprop*(1-Populationprop)/n)

if(z>-E&&z<E){
print("Hospital is not efficient")
}else{
print("Hospital is efficient")
}

# Two sample mean test

xbar=20
ybar=15
n1=500
n2=400
sd=4

z=(xbar-ybar)/(sd*sqrt((1/n1)+(1/n2)))

alpha=0.05
zalpha1=qnorm(1-(alpha/2))

if(z<=zalpha1){
print("Accept null hypothesis")
}else{
print("Reject null hypothesis")
}

# Difference between two proportions

n1=900
n2=1600
p1=0.20
p2=0.185

P=(n1*p1+n2*p2)/(n1+n2)
Q=1-P

z=(p1-p2)/sqrt(P*Q*((1/n1)+(1/n2)))

alpha=0.05
zalpha2=qnorm(1-(alpha/2))

if(z<=zalpha2){
print("accept the null hypothesis")
}else{
print("reject null hypothesis")
}


############################
# LAB 6 — Z SCORE & P TEST
############################

mu0=10000
sigma=120
n=30

z=(xbar-mu0)/(sigma/sqrt(n))

alpha=0.05
zalpha=qnorm(1-alpha)

pval=pnorm(z)
-zalpha

# Problem 2

xbar1=2.1
mu01=2
sigma2=0.25
n=35
alpha=0.05

z1=(xbar1-mu01)/(sigma2/sqrt(n))
zalpha1=qnorm(1-alpha)

pval1=pnorm(z1)
1-pval1

# Problem 3

xbar3=14.6
mu03=15.4
sigma3=2.5
n=35

z3=(xbar3-mu03)/(sigma3/sqrt(n))

alpha=0.05
zhalfalpha=qnorm(1-(alpha/2))
c(-zhalfalpha,zhalfalpha)

pval3=2*pnorm(z3)

p=85/148
p0=60/100
n=148
q0=1-p0

z=(p-p0)/sqrt(p0*q0/n)

alpha=0.05
zalpha=qnorm(1-alpha)
-zalpha

pval=pnorm(z)

# Problem 4

p1=30/214
p0=12/100
n=214

q0=1-p0

z=(p1-p0)/sqrt(p0*q0/n)

alpha=0.05
zalpha=qnorm(1-alpha)

pval=pnorm(z,lower.tail=FALSE)

p=18/30
p0=1/2
q0=1-p0

z=(p-p0)/(sqrt(p0*q0/n))

alpha=0.05
zhalfalpha=qnorm(1-(alpha/2))
c(-zhalfalpha,zhalfalpha)

pval=2*pnorm(z,lower.tail=FALSE)

p=12/30
z=(p-p0)/(sqrt(p0*q0/n))

zhalfalpha=qnorm(1-(alpha/2))
c(-zhalfalpha,zhalfalpha)

pval=2*pnorm(z,lower.tail=FALSE)


'''
