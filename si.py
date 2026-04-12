'''
# --- Visualizations ---


# --- Sample Data ---
x = 1:10
y = c(2,5,3,7,8,6,9,10,12,11)
category = c("A","B","A","B","A","B","A","B","A","B")
df = data.frame(x, y, category)

# --- Basic Plots ---

# 1. Scatter Plot
plot(x, y, main="Scatter Plot", xlab="X", ylab="Y")

# 2. Line Plot
plot(x, y, type="l", col="blue", main="Line Plot")

# 3. Scatter + Line
plot(x, y)
lines(x, y, col="red")

# 4. Multiple Lines
y2 = y + 2
plot(x, y, type="l", col="blue")
lines(x, y2, col="red")

# --- Bar Plots ---

# 5. Simple Bar Plot
barplot(y, main="Bar Plot")

# 6. Named Bar Plot
barplot(y, names.arg=x, col="skyblue")

# 7. Grouped Bar Plot
mat = matrix(c(5,3,4,6,7,2), nrow=2)
barplot(mat, beside=TRUE, col=c("blue","red"))

# 8. Stacked Bar Plot
barplot(mat, col=c("blue","red"))

# --- Pie Chart ---
pie(table(category), main="Pie Chart")

# --- Histogram ---
hist(y, col="lightblue", main="Histogram")

# --- Box Plot ---
boxplot(y, main="Box Plot")

# Boxplot with groups
boxplot(y ~ category, data=df, col=c("pink","lightgreen"))

# --- Density Plot ---
plot(density(y), main="Density Plot")


# --- Legends Example ---
plot(x, y, type="l", col="blue")
lines(x, y2, col="red")
legend("topleft", legend=c("y","y2"), col=c("blue","red"), lty=1)


# --- Type Conversion ---
as.character(4.3)
as.numeric("5")
as.factor(x)



# --- Data Frame ---
df = data.frame(col1 = x, col2 = x+1)
str(df)
summary(df)



# --- Accessing Data ---
df[1,2]
df$col1
nrow(df)
ncol(df)
head(df)


# --- Factors ---
df$status = factor(c(1,2,1,2), labels = c("staff","faculty"))



# --- Tables ---
table(df$col1)
table(df$col1, df$status)
prop.table(table(df$col1))



# --- Plots ---
plot(x, x^2, type = "l")
pie(table(df$col1))
barplot(table(df$col1))
boxplot(x ~ df$status)
hist(x)



# --- Sampling ---
sample(1:50, 5)
sample(1:6, 10, replace = TRUE)
sample(c("H","T"), 10, replace = TRUE)



# --- Probability ---
choose(5,2)
factorial(5)
dbinom(2,5,0.5)
dpois(2,3)



# --- Expectation & Variance ---
xv = c(0,1,2,3)
p = c(1/8,3/8,3/8,1/8)
mean_val = sum(xv*p)
var_val = sum(xv^2*p) - mean_val^2



# --- Z-Test (Manual) ---
xbar = 50
mu = 45
sigma = 10
n = 30
z = (xbar - mu)/(sigma/sqrt(n))
alpha = 0.05
z_crit = qnorm(1 - alpha/2)
pval = 2 * pnorm(z)



# --- Z-Test (Built-in) ---
library(BSDA)
zsum.test(50, 10, 30)



# --- Proportion Test ---
prop.test(30, 100)



# --- T-Test ---
sample_data = c(10,12,9,11,10)
t.test(sample_data)



# --- Two Sample T-Test ---
x1 = c(10,12,11)
x2 = c(9,8,10)
t.test(x1, x2)



# --- Paired T-Test ---
t.test(x1, x2, paired = TRUE)



# --- Chi-Square Test ---
mat = matrix(c(10,20,30,40), nrow=2)
chisq.test(mat)

# --- Variance Test (F-Test) ---
var(x1)/var(x2)
qf(1 - alpha, df1=2, df2=2)

# --- Decision Rule ---
if (pval > alpha) {
  print("Accept H0")
} else {
  print("Reject H0")
}



# =====================================
# MANUAL STATISTICAL TESTS (ALL TYPES)
# =====================================

alpha = 0.05

# -----------------------------
# 1. ONE SAMPLE Z-TEST (MEAN)
# -----------------------------
xbar = 50
mu0 = 45
sigma = 10
n = 30

z = (xbar - mu0)/(sigma/sqrt(n))
z_crit = qnorm(1 - alpha/2)
pval = 2 * pnorm(z)

if (abs(z) < z_crit) {
  print("Accept H0")
} else {
  print("Reject H0")
}

# -----------------------------
# 2. TWO SAMPLE Z-TEST (MEANS)
# -----------------------------
xbar1 = 50
xbar2 = 45
sigma1 = 10
sigma2 = 8
n1 = 30
n2 = 40

z = (xbar1 - xbar2)/sqrt((sigma1^2/n1) + (sigma2^2/n2))
z_crit = qnorm(1 - alpha/2)

if (abs(z) < z_crit) {
  print("Accept H0")
} else {
  print("Reject H0")
}

# -----------------------------
# 3. ONE SAMPLE T-TEST
# -----------------------------
x = c(10,12,9,11,10)

xbar = mean(x)
s = sd(x)
n = length(x)
mu0 = 10

t = (xbar - mu0)/(s/sqrt(n))
t_crit = qt(1 - alpha/2, df=n-1)

if (abs(t) < t_crit) {
  print("Accept H0")
} else {
  print("Reject H0")
}

# -----------------------------
# 4. TWO SAMPLE T-TEST (INDEPENDENT)
# -----------------------------
x1 = c(10,12,11)
x2 = c(9,8,10)

n1 = length(x1)
n2 = length(x2)

xbar1 = mean(x1)
xbar2 = mean(x2)

s1 = var(x1)
s2 = var(x2)

t = (xbar1 - xbar2)/sqrt((s1/n1) + (s2/n2))
t_crit = qt(1 - alpha/2, df=n1+n2-2)

if (abs(t) < t_crit) {
  print("Accept H0")
} else {
  print("Reject H0")
}

# -----------------------------
# 5. PAIRED T-TEST
# -----------------------------
a = c(12,23,5,18,10)
b = c(18,22,15,21,13)

d = b - a
n = length(d)

dbar = mean(d)
sd = sqrt(var(d))

t = dbar/(sd/sqrt(n))
t_crit = qt(1 - alpha, df=n-1)

if (t < t_crit) {
  print("Accept H0")
} else {
  print("Reject H0")
}

# -----------------------------
# 6. ONE PROPORTION Z-TEST
# -----------------------------
x = 40
n = 100

p_hat = x/n
p0 = 0.5
q0 = 1 - p0

z = (p_hat - p0)/sqrt(p0*q0/n)
z_crit = qnorm(1 - alpha/2)

if (abs(z) < z_crit) {
  print("Accept H0")
} else {
  print("Reject H0")
}

# -----------------------------
# 7. TWO PROPORTION Z-TEST
# -----------------------------
x1 = 40; n1 = 100
x2 = 30; n2 = 80

p1 = x1/n1
p2 = x2/n2

p = (x1 + x2)/(n1 + n2)
q = 1 - p

z = (p1 - p2)/sqrt(p*q*(1/n1 + 1/n2))
z_crit = qnorm(1 - alpha/2)

if (abs(z) < z_crit) {
  print("Accept H0")
} else {
  print("Reject H0")
}

# -----------------------------
# 8. CHI-SQUARE TEST
# -----------------------------
obs = c(20, 30, 50)
exp = c(25, 25, 50)

chi = sum((obs - exp)^2/exp)
df = length(obs) - 1

chi_crit = qchisq(1 - alpha, df)

if (chi < chi_crit) {
  print("Accept H0")
} else {
  print("Reject H0")
}

# -----------------------------
# 9. F-TEST (VARIANCE)
# -----------------------------
x = c(10,12,11,13)
y = c(9,8,10,7)

F = var(x)/var(y)

df1 = length(x)-1
df2 = length(y)-1

F_crit = qf(1 - alpha, df1, df2)

if (F < F_crit) {
  print("Accept H0")
} else {
  print("Reject H0")
}  

'''
