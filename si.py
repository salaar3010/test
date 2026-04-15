#exp 10 kruskal test
x = c(10,11,12,13,14)
y = c(20,22,25,26,27)
z = c(33,34,35,36,37)

values = c(x,y,z)
values
group = factor(c(
  rep('x',length(x)),
  rep('y',length(y)),
  rep('z',length(z))
))
group

kruskal.test(values ~ group)

boxplot(values ~ group)

rank = rank(values)
rank
mean_rank = tapply(rank,group,mean)
mean_rank

plot(mean_rank)
plot(density(x))
lines(density(y))
lines(density(z))

# exp 9 k-s test Kolmogorov–Smirnov 
#one sample

x = c(2.1, 2.5, 3.0, 3.5, 4.0, 2.8, 3.2, 3.7, 2.9, 3.4)

ks.test(x,'pnorm',mean= mean(x), sd = sd(x))
plot(ecdf(x))
curve(pnorm(x,mean = mean(x),sd=sd(x)),add = T)
hist(x)
curve(dnorm(x,3,1),add = T)

#exp 8
#median test

a = c(1,2,3,4,5,6,7,8,9,10)
b = c(3,4,5,6,1,2,7,8,9,10)
c = c(12,43,23,56,76,22,0,1,2)
data =c(a,b,c)

group =factor(c(
  rep('a',length(a)),
  rep('b',length(b)),
  rep('c',length(c))
))

alpha = 0.05
median_val = median(data)
median_val
tbl = table(group,data > median_val)
tbl
test = chisq.test(tbl)
test
if(test$p.value < alpha) print("reject H0") else print("Accept H0")

boxplot(a,b,c)
plot(density(a))
lines(density(b))
lines(density(c))
hist(a)
hist(b,add = T)
hist(c,add = T)

plot(data)
abline(h = median_val)

#exp 7 sign test
data =c(3,5,7,9,11,13)
mo = 15

signs = sign(data - mo)
signs
sings = signs[signs != 0]
s = sum(sings>0)
n =length(sings)
pvalue = binom.test(s,n-s,p = 0.5)


if (pvalue$p.value < 0.05) print('Reject H0')
plot(data)
abline(h = mo,col = 'red')
barplot(data)
x = 0:n
prob = dbinom(x, n, 0.5)

barplot(prob,
        names.arg=x,
        col="skyblue",
        main="Binomial Distribution",
        xlab="Positive Signs",
        ylab="Probability")

#exp 6 categorical cate chi test
data = matrix(c(40,50,45,55),nrow = 2)
rownames(data) =c('young','old')
colnames(data) =c('online shopping','offline')

test = chisq.test(data)
critical =qchisq(0.95,1)
if (test$p.value > critical) print("Reject H0") else print("accept H0")
barplot(data,beside = T)

mosaicplot(data)
assocplot(data)

#exp5
n = 4
N = 160
p =0.5
x =0:n
obf = c(8,16,12,46,10)
prob = dbinom(x,n,p)
test =chisq.test(obf,p = prob)

if  (test$p.value < 0.05) print("reject h0") else print('Accept H0')
y = dchisq(x, df=4)

plot(x, y, type="l", lwd=2,
     main="Chi-square Distribution")

cv = qchisq(0.95, df=4)

# Shade rejection region
polygon(c(cv, x[x>=cv], max(x)),
        c(0, y[x>=cv], 0),
        col="red")

abline(v=cv, col="blue", lty=2)

#exp 4
x = rnorm(15, mean=0, sd=sqrt(36))  # s1² = 36
y = rnorm(12, mean=0, sd=sqrt(16))  # s2² = 16

test = var.test(x, y)
if(test$p.value < 0.05){
  "Reject H0"
}else{
  "Fail to Reject H0"
}
xv = seq(0, 6, length=1000)
yv = df(xv, df1=14, df2=11)

plot(xv, yv, type="l", lwd=2,
     main="F Distribution")

cv = qf(0.95, 14, 11)

polygon(c(cv, xv[xv>=cv], max(xv)),
        c(0, yv[xv>=cv], 0),
        col="red")

abline

#rest
# Z test (use t.test if sigma unknown)
x = rnorm(64, mean=105, sd=15)
t.test(x, mu=100)

# 🔹 Visualization
xv = seq(-4, 4, length=1000)
yv = dnorm(xv)

plot(xv, yv, type="l", lwd=2,
     main="Z Distribution", xlab="Z", ylab="Density")

alpha = 0.05
z_crit = qnorm(1 - alpha/2)

polygon(c(xv[xv <= -z_crit], -z_crit),
        c(yv[xv <= -z_crit], 0),
        col="red")

polygon(c(z_crit, xv[xv >= z_crit]),
        c(0, yv[xv >= z_crit]),
        col="red")

abline(v=c(-z_crit, z_crit), col="blue", lty=2)

#T-TEST
# One-sample t-test
x = c(1.01,0.97,1.03,1.04,0.99,0.98,0.99,1.01,1.03)
t.test(x)

# 🔹 Visualization
xv = seq(-4, 4, length=1000)
yv = dt(xv, df=length(x)-1)

plot(xv, yv, type="l", lwd=2,
     main="t Distribution", xlab="t", ylab="Density")

alpha = 0.05
t_crit = qt(1 - alpha/2, df=length(x)-1)

polygon(c(xv[xv <= -t_crit], -t_crit),
        c(yv[xv <= -t_crit], 0),
        col="red")

polygon(c(t_crit, xv[xv >= t_crit]),
        c(0, yv[xv >= t_crit]),
        col="red")

abline(v=c(-t_crit, t_crit), col="blue", lty=2)

#chi
# Observed data
obf = c(8,42,68,32,10)

# Expected probabilities
prob = dbinom(0:4, 4, 0.5)

# Test
chisq.test(obf, p=prob)

# 🔹 Visualization
xv = seq(0, 20, length=1000)
yv = dchisq(xv, df=4)

plot(xv, yv, type="l", lwd=2,
     main="Chi-square", xlab="Chi-square", ylab="Density")

cv = qchisq(0.95, df=4)

polygon(c(cv, xv[xv>=cv], max(xv)),
        c(0, yv[xv>=cv], 0),
        col="red")

abline(v=cv, col="blue", lty=2)

#f
# Sample data
x = rnorm(15, sd=sqrt(36))
y = rnorm(12, sd=sqrt(16))

# Test
var.test(x, y)

# 🔹 Visualization
xv = seq(0, 6, length=1000)
yv = df(xv, df1=14, df2=11)

plot(xv, yv, type="l", lwd=2,
     main="F Distribution", xlab="F", ylab="Density")

cv = qf(0.95, 14, 11)

polygon(c(cv, xv[xv>=cv], max(xv)),
        c(0, yv[xv>=cv], 0),
        col="red")

abline(v=cv, col="blue", lty=2)



# prop Test
prop.test(130, 400, p=0.30)

# 🔹 Visualization (normal approx)
xv = seq(-4, 4, length=1000)
yv = dnorm(xv)

plot(xv, yv, type="l", lwd=2,
     main="Proportion Test", xlab="Z", ylab="Density")

z_crit = qnorm(0.975)

polygon(c(xv[xv <= -z_crit], -z_crit),
        c(yv[xv <= -z_crit], 0),
        col="red")

polygon(c(z_crit, xv[xv >= z_crit]),
        c(0, yv[xv >= z_crit]),
        col="red")

abline(v=c(-z_crit, z_crit), col="blue", lty=2)
