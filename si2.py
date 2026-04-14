# =========================
# LAB 1 – HYPOTHESIS TESTS
# =========================
library(BSDA)

zsum.test(501,112,500,conf.level=0.99)
zsum.test(42,8,75,36,6,50,mu=0,conf.level=0.96)

tsum.test(mean.x=3.11,s.x=0.771,n.x=12,
          mean.y=2.04,s.y=0.448,n.y=10,
          var.equal=TRUE,conf.level=0.90)

x=c(1.01,0.97,1.03,1.04,0.99,0.98,0.99,1.01,1.03)
t.test(x,conf.level=0.99)

CI.sim(samples=50,n=20,mu=100,sigma=5,
       conf.level=0.95,type="mean")

prop.test(c(75,80),c(1500,2000),conf.level=0.90,correct=FALSE)

P_A=c(3.5,2.7,3.9,4.2,3.6,2.7,3.3,5.2,4.2,2.9,4.4,5.2,4.0,4.1,3.4)
P_B=c(4.7,3.9,4.5,5.5,4.0,5.3,4.3,6.0,5.2,3.7,5.5,6.2,5.1,5.4,4.8)
t.test(P_B,P_A,var.equal=TRUE)

# =========================
# LAB 2 – VISUALIZATION
# =========================

# mtcars
x=c('A','B','C','D','E','F')
y=c(2,4,6,8,10,3)

barplot(y,names.arg=x,col='blue',main='Barplot')
barplot(table(mtcars$cyl),main='No of Cylinders')

boxplot(mtcars$mpg,col='yellow',main='MPG Boxplot')

boxplot(mpg~gear,data=mtcars,
        col=c('lightgreen','green','darkgreen'),
        main='MPG vs Gear')

hist(mtcars$mpg,col='yellow',main='Histogram')
hist(mtcars$mpg,col='green',breaks=10,border='red')

den=density(mtcars$mpg)
plot(den,type='p',col='red',main='Density Plot')

pie(table(mtcars$gear),main='Gears')

plot(cars$speed,cars$dist,
     main='Speed vs Distance',
     col='pink',pch=15)

# iris
barplot(table(iris$Species),col='lightblue',main='Species Count')

boxplot(iris$Sepal.Length,col='yellow',main='Sepal Length')

boxplot(Sepal.Length~Species,data=iris,
        col=c('lightgreen','green','darkgreen'),
        main='Sepal vs Species')

hist(iris$Sepal.Length,col='yellow')
den=density(iris$Sepal.Length)
plot(den,type='p',col='red')

pie(table(iris$Species),main='Species Pie')

plot(iris$Sepal.Length,iris$Petal.Length,
     col='purple',pch=15,
     main='Sepal vs Petal')

# airquality
data(airquality)

barplot(table(airquality$Month),col='skyblue',
        main='Month Count')

boxplot(airquality$Ozone,col='yellow',
        main='Ozone Boxplot')

boxplot(Ozone~Month,data=airquality,
        col=c("lightgreen","green","darkgreen","lightblue","orange"))

hist(airquality$Ozone,col='yellow')

den=density(na.omit(airquality$Ozone))
plot(den,type='p',col='red')

# =========================
# EXPERIMENT 3 – LARGE SAMPLE TEST
# =========================

xbar=105; mu0=100; s=15; n=64
z=(xbar-mu0)/(s/sqrt(n))
z
2*(1-pnorm(abs(z)))

x=rnorm(64,105,15)
t.test(x,mu=100)

z_vals=seq(-4,4,length=1000)
dens=dnorm(z_vals)
alpha=0.05
z_crit=qnorm(1-alpha/2)

plot(z_vals,dens,type="l",main="Z Test",xlab="Z",ylab="Density")
abline(v=c(-z_crit,z_crit),col="red",lty=2)
abline(v=z,col="blue")
legend("topright",legend=c("Critical","Observed"),
       col=c("red","blue"),lty=c(2,1))

# two mean
xbar1=520;xbar2=500;s1=80;s2=75;n1=100;n2=120
z=(xbar1-xbar2)/sqrt((s1^2/n1)+(s2^2/n2))
z
2*(1-pnorm(abs(z)))

x1=rnorm(100,520,80)
x2=rnorm(120,500,75)
t.test(x1,x2)

plot(z_vals,dens,type="l",main="Two Mean Z")
abline(v=c(-z_crit,z_crit),col="red",lty=2)
abline(v=z,col="blue")

# =========================
# EXPERIMENT 4 – F TEST (WITH GRAPH)
# =========================

s1_sq=36;s2_sq=16;n1=15;n2=12;alpha=0.05
f_cal=s1_sq/s2_sq
df1=n1-1;df2=n2-1

f_upper=qf(1-alpha,df1,df2)
x=seq(0,6,length=1000)
y=df(x,df1,df2)

plot(x,y,type="l",main="F Distribution",xlab="f value",ylab="density")

x_right=seq(f_upper,6,length=500)
y_right=df(x_right,df1,df2)

polygon(c(f_upper,x_right,6),c(0,y_right,0),col="red")
abline(v=f_upper,lty=2)
abline(v=f_cal,col="blue")

# =========================
# EXPERIMENT 5 – CHI SQUARE
# =========================

n=4;alpha=0.05;N=160;p=0.5
x=c(0:n)
obf=c(8,42,68,32,10)
exf=dbinom(x,n,p)*160

chisq=sum((obf-exf)^2/exf)
tv=qchisq(1-alpha,n)

if(chisq<tv){print("Accept H0")}else{print("Reject H0")}

# =========================
# EXPERIMENT 6 – CHI PLOTS
# =========================

data1=matrix(c(45,55,30,70),nrow=2,byrow=TRUE)
barplot(data1,beside=TRUE,col=c("steelblue","orange"),
        main="Barplot")

mosaicplot(data1,color=TRUE,main="Mosaic Plot")
assocplot(data1,main="Association Plot")

# =========================
# EXPERIMENT 7 – SIGN & RANK
# =========================

data=c(8,11,13,17,19,21,24)
M0=15
signs=sign(data-M0)
signs=signs[signs!=0]

S=sum(signs>0)
n=length(signs)

p_value=2*pbinom(min(S,n-S),n,0.5)

x=0:n
prob=dbinom(x,n,0.5)
barplot(prob,names.arg=x,main="Binomial Distribution")

plot(data,pch=8,main="Sign Visualization")
abline(h=M0,lty=2)

pos=sum(signs>0)
neg=sum(signs<0)
pie(c(pos,neg),labels=c("Positive","Negative"),
    main="Sign Distribution")

dotchart(data,main="Dotchart")
abline(v=M0,lty=2)

before=c(20,22,25,27,30)
after=c(23,24,26,29,32)

wilcox.test(after,before,paired=TRUE)

plot(before,after,pch=19,main="Before vs After")
abline(0,1)

boxplot(before,after,names=c("Before","After"),
        main="Comparison")

d=after-before
dotchart(d,main="Differences")
abline(v=0,lty=2)

# =========================
# EXPERIMENT 8 – MEDIAN TEST
# =========================

A=c(12,15,14,10,13,16,18,17,19,11)
B=c(18,20,17,22,19,21,23,24,16,25)
C=c(11,13,15,16,14,12,17,18,19,20)
D=c(21,23,19,24,22,25,26,27,20,28)

data=c(A,B,C,D)
group=factor(c(rep("A",10),rep("B",10),rep("C",10),rep("D",10)))

median_val=median(data)
tbl=table(group,data>median_val)
chisq.test(tbl)

boxplot(A,B,C,D,names=c("A","B","C","D"),
        main="Median Test Boxplot")
abline(h=median_val,lty=2)

plot(density(A),col='blue',main="Density Plot")
lines(density(B),col='red')
lines(density(C),col='green')
lines(density(D),col='purple')

hist(A,col=rgb(0,0,1,0.4),main="Histogram Comparison")
hist(B,col=rgb(1,0,0,0.4),add=TRUE)
hist(C,col=rgb(0,1,0,0.4),add=TRUE)
hist(D,col=rgb(0.5,0,0.5,0.4),add=TRUE)

# =========================
# EXPERIMENT 9 – KS TEST
# =========================

x=c(2.1,2.5,3.0,3.5,4.0,2.8,3.2,3.7,2.9,3.4)

ks.test(x,"pnorm",mean=3,sd=1)

plot(ecdf(x),main="ECDF vs CDF")
curve(pnorm(x,3,1),add=TRUE,col="red")

plot(ecdf(x),verticals=TRUE,do.points=FALSE,
     main="Step ECDF",col="blue")

hist(x,probability=TRUE,main="Histogram")
curve(dnorm(x,3,1),add=TRUE,col="red")

xx=seq(min(x),max(x),length=100)
plot(xx,abs(ecdf(x)(xx)-pnorm(xx,3,1)),
     type="l",main="Absolute Difference")

# two sample
x=c(12,15,14,10,13,16,18,17,19,11)
y=c(18,20,17,22,19,21,23,24,18,20)

ks.test(x,y)

plot(ecdf(x),col="blue",main="ECDF Comparison")
lines(ecdf(y),col="red")

hist(x,probability=TRUE,col=rgb(0,0,1,0.5))
hist(y,probability=TRUE,col=rgb(1,0,0,0.5),add=TRUE)

# =========================
# EXPERIMENT 10 – KRUSKAL
# =========================

x=c(8,12,10,9,11)
y=c(15,18,17,16,19)
z=c(22,25,24,23,26)

values=c(x,y,z)
group=factor(c(rep("x",5),rep("y",5),rep("z",5)))

kruskal.test(values~group)

boxplot(values~group,col=c("red","green","blue"),
        main="Kruskal Boxplot")

ranks=rank(values)
mean_rank=tapply(ranks,group,mean)

plot(mean_rank,type="b",pch=19,
     main="Mean Rank Comparison")

plot(density(x),col='red',main="Density Comparison")
lines(density(y),col='green')
lines(density(z),col='blue')