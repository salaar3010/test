# ================= EXP-1: Correlation =================
library(ggplot2)
library(corrplot)
library(PerformanceAnalytics)

data = mtcars

ggplot(data, aes(wt, mpg)) + geom_point() + geom_smooth(method="lm")

cor(data$wt, data$mpg)

corrplot(cor(data[,c("mpg","disp","hp","wt")]))

chart.Correlation(data[,c("mpg","disp","hp","wt")])


# ================= EXP-2: Simple Linear Regression =================
data(cars)

model = lm(dist ~ speed, data=cars)

plot(cars$speed, cars$dist)
abline(model, col="red")

summary(model)
anova(model)

newdata = data.frame(speed=15)
predict(model, newdata)
predict(model, newdata, interval="confidence")
predict(model, newdata, interval="predict")


# ================= EXP-3: Residual + Forecast =================
library(forecast)

data("AirPassengers")

fit = lm(AirPassengers ~ time(AirPassengers))
plot(AirPassengers)
abline(fit, col="red")

plot(fit)

train = window(AirPassengers, end=c(1956,12))
plot(train)
lines(meanf(train, h=48)$mean, col=2)
lines(rwf(train, h=48)$mean, col=4)


# ================= EXP-4: Hypothesis Testing =================
model = lm(dist ~ speed, data=cars)
s = summary(model)

p_value = s$coefficients[2,4]

if(p_value < 0.05) print("Reject H0") else print("Accept H0")

f_val = s$fstatistic[1]
f_tab = qf(0.95, s$fstatistic[2], s$fstatistic[3])

if(f_val > f_tab) print("Reject H0") else print("Accept H0")

confint(model)


# ================= EXP-5: Prediction & Multiple Regression =================
model = lm(dist ~ speed, data=cars)

new = data.frame(speed=c(10,20,25))
predict(model, new)
predict(model, new, interval="confidence")
predict(model, new, interval="predict")

data(stackloss)
model2 = lm(stack.loss ~ Air.Flow + Water.Temp + Acid.Conc, data=stackloss)

newdata = data.frame(Air.Flow=72, Water.Temp=20, Acid.Conc=85)
predict(model2, newdata)


# ================= EXP-6: Multiple Regression + AIC =================
library(MASS)

data(mtcars)

model = lm(mpg ~ ., data=mtcars)
summary(model)

plot(model)

stepAIC(model)

model2 = lm(mpg ~ wt + qsec + am, data=mtcars)

new = data.frame(wt=2.9, qsec=20, am=1)
predict(model2, new, interval="predict")


# ================= EXP-7: Multicollinearity =================
library(olsrr)
library(corrplot)

data = mtcars[,c("mpg","cyl","disp","hp","wt")]

model = lm(mpg ~ ., data=data)

corrplot(cor(data))

ols_vif_tol(model)
ols_eigen_cindex(model)


# ================= EXP-8: (If clustering/hierarchical used earlier) =================
# (Optional – based on your syllabus)
# Example:
# dist_data = dist(scale(mtcars))
# hc = hclust(dist_data)
# plot(hc)


# ================= EXP-9: Time Series (AR, MA) =================
data(AirPassengers)

ts.plot(AirPassengers)
acf(AirPassengers)

AR = arima(AirPassengers, order=c(1,0,0))
MA = arima(AirPassengers, order=c(0,0,1))

predict(AR, n.ahead=10)
predict(MA, n.ahead=10)

AIC(AR); AIC(MA)
BIC(AR); BIC(MA)


# ================= EXP-10: Non-linear Regression =================
library(minpack.lm)

# Polynomial
hwc = c(0,2,3,4,5,5,5,6,6,5,7,8,9,10,11,12,13,14)
ts = c(15,20,24,26,30,34,38,40,42,47,53,52,53,49,43,27,22,25)

plot(hwc, ts)

curve(predict(lm(ts ~ hwc + I(hwc^2)), data.frame(hwc=x)),
      add=TRUE, col="blue")

# nls
data(Puromycin)
plot(rate ~ conc, data=Puromycin)

model = nls(rate ~ (a*conc)/(b+conc),
            data=Puromycin,
            start=list(a=200,b=0.1))

curve(predict(model, data.frame(conc=x)),
      add=TRUE, col="green")

# nlsLM
week = 1:16
mass = c(4,8,12,13,15,18,19,8,21.3,21,22,23,24.3,24.8,25,25.5)

plot(week, mass)

model2 = nlsLM(mass ~ a*(1-exp(-b*week)),
               start=list(a=max(mass), b=0.2))

curve(predict(model2, data.frame(week=x)),
      add=TRUE, col="red")

# Load dataset
data(AirPassengers)

# Basic info
is.ts(AirPassengers)
summary(AirPassengers)
start(AirPassengers)
end(AirPassengers)
frequency(AirPassengers)

# Plot time series
ts.plot(AirPassengers, xlab="Year", ylab="Passengers",
        main="AirPassengers Time Series")

# Add trend line
abline(lm(AirPassengers ~ time(AirPassengers)), col="red")

# Autocorrelation
acf(AirPassengers, main="ACF of AirPassengers")

# ================= AR MODEL =================
AR = arima(AirPassengers, order=c(1,0,0))
AR

# Fitted values
AR_fit = AirPassengers - residuals(AR)

# Plot AR fit
ts.plot(AirPassengers, main="AR Model Fit")
lines(AR_fit, col="blue", lwd=2)

# Forecast (next 10 values)
AR_forecast = predict(AR, n.ahead=10)$pred
AR_se = predict(AR, n.ahead=10)$se

# Plot forecast
ts.plot(AirPassengers, xlim=c(1949,1962), main="AR Forecast")
lines(ts(AR_forecast, start=1961, frequency=12), col="blue", lwd=2)
lines(ts(AR_forecast + 2*AR_se, start=1961, frequency=12), col="blue", lty=2)
lines(ts(AR_forecast - 2*AR_se, start=1961, frequency=12), col="blue", lty=2)

# ================= MA MODEL =================
MA = arima(AirPassengers, order=c(0,0,1))
MA

# Fitted values
MA_fit = AirPassengers - residuals(MA)

# Plot MA fit
ts.plot(AirPassengers, main="MA Model Fit")
lines(MA_fit, col="red", lwd=2)

# Forecast (next 10 values)
MA_forecast = predict(MA, n.ahead=10)$pred
MA_se = predict(MA, n.ahead=10)$se

# Plot forecast
ts.plot(AirPassengers, xlim=c(1949,1962), main="MA Forecast")
lines(ts(MA_forecast, start=1961, frequency=12), col="red", lwd=2)
lines(ts(MA_forecast + 2*MA_se, start=1961, frequency=12), col="red", lty=2)
lines(ts(MA_forecast - 2*MA_se, start=1961, frequency=12), col="red", lty=2)

# ================= MODEL COMPARISON =================
cor(AR_fit, MA_fit)

AIC(AR)
AIC(MA)

BIC(AR)
BIC(MA)
