'''

1. Confidence Interval (Mean)
# Input
mean <- as.numeric(readline("Enter sample mean: "))
sd <- as.numeric(readline("Enter standard deviation: "))
n <- as.numeric(readline("Enter sample size: "))
z <- as.numeric(readline("Enter z value (1.96 for 95%): "))

# Calculation
margin <- z * (sd / sqrt(n))
lower <- mean - margin
upper <- mean + margin

# Output
cat("Confidence Interval:", lower, "to", upper)

2. P-value (Z test)
# Input
x_bar <- as.numeric(readline("Sample mean: "))
mu <- as.numeric(readline("Population mean: "))
sigma <- as.numeric(readline("Std deviation: "))
n <- as.numeric(readline("Sample size: "))

# Z value
z <- (x_bar - mu) / (sigma / sqrt(n))

# P-value (two-tailed)
p_value <- 2 * (1 - pnorm(abs(z)))

# Output
cat("Z:", z, "\nP-value:", p_value)

3. Large Sample Test (Mean)
# Input
x_bar <- as.numeric(readline("Sample mean: "))
mu <- as.numeric(readline("Population mean: "))
sigma <- as.numeric(readline("Std deviation: "))
n <- as.numeric(readline("Sample size: "))
alpha <- as.numeric(readline("Alpha: "))

# Z test
z <- (x_bar - mu) / (sigma / sqrt(n))
z_crit <- qnorm(1 - alpha/2)

cat("Z:", z, "\nCritical Z:", z_crit)

if(abs(z) > z_crit){
  cat("\nReject Null Hypothesis")
} else {
  cat("\nFail to Reject Null Hypothesis")
}

4. Large Sample Test (Proportion)
# Input
p_hat <- as.numeric(readline("Sample proportion: "))
p <- as.numeric(readline("Population proportion: "))
n <- as.numeric(readline("Sample size: "))
alpha <- as.numeric(readline("Alpha: "))

# Z test
z <- (p_hat - p) / sqrt((p * (1 - p)) / n)
z_crit <- qnorm(1 - alpha/2)

cat("Z:", z, "\nCritical Z:", z_crit)

if(abs(z) > z_crit){
  cat("\nReject Null Hypothesis")
} else {
  cat("\nFail to Reject Null Hypothesis")
}

5. Small Sample Test (t-test for Mean)
# Input
x_bar <- as.numeric(readline("Sample mean: "))
mu <- as.numeric(readline("Population mean: "))
s <- as.numeric(readline("Sample SD: "))
n <- as.numeric(readline("Sample size: "))
alpha <- as.numeric(readline("Alpha: "))

# t test
t_stat <- (x_bar - mu) / (s / sqrt(n))
df <- n - 1
t_crit <- qt(1 - alpha/2, df)

cat("t:", t_stat, "\nCritical t:", t_crit)

if(abs(t_stat) > t_crit){
  cat("\nReject Null Hypothesis")
} else {
  cat("\nFail to Reject Null Hypothesis")
}

6. Paired t-test
# Input
n <- as.numeric(readline("Number of pairs: "))
d <- c()

for(i in 1:n){
  x <- as.numeric(readline("Before: "))
  y <- as.numeric(readline("After: "))
  d[i] <- x - y
}

mean_d <- mean(d)
sd_d <- sd(d)

t_stat <- mean_d / (sd_d / sqrt(n))
df <- n - 1
alpha <- 0.05
t_crit <- qt(1 - alpha/2, df)

cat("t:", t_stat, "\nCritical t:", t_crit)

if(abs(t_stat) > t_crit){
  cat("\nReject Null Hypothesis")
} else {
  cat("\nFail to Reject Null Hypothesis")
}

7. F-test (Variance)
# Input
s1 <- as.numeric(readline("Variance 1: "))
s2 <- as.numeric(readline("Variance 2: "))
n1 <- as.numeric(readline("Sample size 1: "))
n2 <- as.numeric(readline("Sample size 2: "))
alpha <- as.numeric(readline("Alpha: "))

# Ensure s1 > s2
if(s2 > s1){
  temp <- s1; s1 <- s2; s2 <- temp
  temp <- n1; n1 <- n2; n2 <- temp
}

F <- s1 / s2
df1 <- n1 - 1
df2 <- n2 - 1

F_crit <- qf(1 - alpha, df1, df2)

cat("F:", F, "\nCritical F:", F_crit)

if(F > F_crit){
  cat("\nReject Null Hypothesis")
} else {
  cat("\nFail to Reject Null Hypothesis")
}

8. Chi-square (Goodness of Fit)
# Input
observed <- as.numeric(strsplit(readline("Observed: "), " ")[[1]])
expected <- as.numeric(strsplit(readline("Expected: "), " ")[[1]])

chi_stat <- sum((observed - expected)^2 / expected)

df <- length(observed) - 1
alpha <- 0.05

chi_crit <- qchisq(1 - alpha, df)

cat("Chi-square:", chi_stat, "\nCritical value:", chi_crit)

if(chi_stat > chi_crit){
  cat("\nReject Null Hypothesis")
} else {
  cat("\nFail to Reject Null Hypothesis")
}

9. Chi-square (Independence)# Input
r <- as.numeric(readline("Rows: "))
c <- as.numeric(readline("Columns: "))

obs <- matrix(0, r, c)

cat("Enter values row-wise:\n")
for(i in 1:r){
  obs[i, ] <- as.numeric(strsplit(readline(), " ")[[1]])
}

row_totals <- rowSums(obs)
col_totals <- colSums(obs)
total <- sum(obs)

expected <- outer(row_totals, col_totals) / total

chi_stat <- sum((obs - expected)^2 / expected)

df <- (r - 1) * (c - 1)
alpha <- 0.05

chi_crit <- qchisq(1 - alpha, df)

cat("Chi-square:", chi_stat, "\nCritical value:", chi_crit)

if(chi_stat > chi_crit){
  cat("\nReject Null Hypothesis")
} else {
  cat("\nFail to Reject Null Hypothesis")
}


#hack
t.test(data, mu = value)                  # One-sample t-test
t.test(x, y, paired = TRUE)              # Paired t-test
prop.test(x, n, p = value)               # Proportion test
chisq.test(observed)                     # Chi-square GOF
chisq.test(matrix)                       # Independence test
var.test(x, y)                           # F-test
'''
