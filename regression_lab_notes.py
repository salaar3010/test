
'''
 EXP-1:-Correlation an alysis using scatter diagram , karl pearson s correlation  coefficient and 
 drawing inferences  

 library(tidyverse)  
 ggplot(iris, aes(x=Sepal.Width, y = Sepal.Length)) +  
   facet_wrap(~Species,scale="free_x") +  
   geom_point() +  
   geom_smooth(formula = y ~ x, method = "lm", se = FALSE) +  
   labs(x = "Sepal Width",y  = "Sepal Length",title = "Sepal Length",subtitle = "grouped by species")  
 my_data = mtcars  
 my_data  
 cor_1 = cor.test(my_data$wt, my_data$mpg)  
 cor_1  
 my_data1 = mtcars[,c(1,3,4,5)]  
 my_data1  
 head(my_data1,5)  
 cor_2 = round(cor(my_data1,method = "pearson"),4)  
 cor_2  
 library(corrplot)  
 my_data2= mtcars[,c(1,3,4,5)]  
 my_data2  
 cor_3 = corrplot(cor_2,type="upper",order = "hclust",tl.col = "blue")  
 cor_3  
 library(PerformanceAnalytics)  
 my_data3= mtcars[,c(1,3,4,5)]  
 cor_4 = chart.Correlation(my_data3,histogram = TRUE,method = "pearson")  
 cor_4  
  
  



 EXP-2:-Simple linear regression – mod el fitting , estima tion of parameters , c omputing R2 and 
 adjusted R2 and m odel intepretation  

 cars 
 summary(cars)  
 speed = cars$speed  
 speed_bar = mean(speed)  
 speed_bar  
 dist = cars$dist  
 dist_bar = mean(dist)  
 dist_bar  
 s_speed = sd(speed)  
 s_speed  
 s_dist = sd(dist)  
 s_dist  
  
 plotting scatter plot  
 plot(speed,dist,xlab="speed",ylab="distance",main="Speed vs distance",col="blue")  
  simple linear regression  
 slr=lm(dist~speed)  
 slr 
  draw the fitted line in the plot  
 abline(slr,col="red")  
  error assumption --- normally distributed  
 residual=slr$residuals  
 hist(residual,col="blue")  
  variance of residual  
 plot(slr$residual~speed)  
 abline(0,0)  
  summary of slr  
 summary(slr)  
  anova  
 anova(slr)  
 table value of f  
 ft=qf(0.95,df1=1,df2=48)  
 ft 
  p value approach  
 pv=1 -pf(89.567,1,48)  
 pv 
  confidence interval  
 confint(slr,level=0.95)  
  doing new prediction  
 new_data=data.frame(speed=15)  
 conf=predict(slr,new_data,interval="confidence")  
 conf  
 pred=predict(slr,new_data,interval="predict")  
 pred  


 EXP-3:-Residual analys is and fo recast for a given dataset  

 install.packages("UsingR")  
 library(UsingR)  
 data('diamond')  
 mydata = diamond  
 mydata  
 plot(mydata$carat,mydata$price,  
      ylab="price",xlab ="Carat")  
 fit = lm(mydata$price~mydata$carat)  
 fit 
  
 abline(fit,col="red")  
 library(broom)  
 library(ggplot2)  
 model.diag.metrics=augment(fit)  
 head(model.diag.metrics)  
 ggplot(model.diag.metrics,aes(mydata$carat,mydata$price)) + geom_point() +  
   stat_smooth(method = lm,se=F)+  
   geom_segment(aes(xend=mydata$carat,yend=.fitted),color = "red",size=0.5)  
 plot(fit,1)  
 plot(fit,2)  
 plot(fit,3)  
 plot(fit,4)  
 plot(fit,5)  
  
 forecasting  
 library(forecast)  
 data('AirPassengers')  
 class(AirPassengers)  
 frequency(AirPassengers)  
 series = AirPassengers  
 series  
 plot(series,col='darkblue',ylab='Passengers on airplanes')  
 boxplot(split(series,cycle(series)),names=month.abb,col='darkgreen')  
 train_set = window(series,start=1949,end=c(1956,12))  
 train_set  
 test_set= window(series,start=1957,end=c(1960,12))  
 test_set  
 plot(train_set,main="Air passengers")  
 forecasting for 4 years  
 lines(meanf(train_set,h=48)$mean,col=4)  
 lines(rwf(train_set,h=48)$mean,col=2)  



 EXP-4:-validati ng linear model using t,f and p test  

 data(cars)  
 cars 
 scatter.smooth(x=cars$speed,y=cars$dist,main='dist vs speed')  
 par(mfrow=c(1,2))  
 boxplot(cars$speed,main = "Speed",  
         sub=paste("Outlier rows:",boxplot.stats(cars$speed)$out),col='gold')  
 boxplot(cars$dist,main = "Distance",  
         sub=paste("Outlier rows:",boxplot.stats(cars$dist)$out),col="gold")  
 cor(cars$speed,cars$dist)  
 linear_model =lm(dist~speed,data=cars)  
 linear_model  
 model_summary = summary(linear_model)  
 model_summary  
 modelcoeffs = model_summary$coefficients  
 modelcoeffs  
 n = nrow(cars)  
 beta.estimate = modelcoeffs['speed','Estimate']  
 beta.estimate  
 std.error = modelcoeffs['speed','Std. Error']  
 std.error  
 alpha= 0.05  
 t_value = beta.estimate/std.error  
 t_value  
 t_table= qt((alpha/2),n -2,lower.tail=F)  
 t_table  
 p_value = 2*pt( -abs(t_value),df=nrow(cars) -ncol(cars))  
 p_value  
 if(p_value < 0.05) print('Reject Null hypothesis that the coeffecient of the predictor is zero') else 
 print("Accept the null hypothesis")  
 f = summary(linear_model)$fstatistic  
 f 
 f_table = qf(0.95,df1 = f[2],df2=f[3])  
 f_table  
  
 if (f[1] > f_table) print("Reject the null hypothesis that the coeffecient of the predictor is zero") else 
 print("Accept the null hypothesis")  
 summary(linear_model)$r.squared  
 summary(linear_model)$adj.r.squared  
 confint(linear_model)  



 EXP-5:-Devoloping confidence interval and testing the model for simp le and m ultiple regression  

 data('cars')  
 cars 
 lin_mod = lm(dist~speed ,data=cars)  
 lin_mod  
  Creating new data  
 new_speeds = data.frame(speed=c(13,20,25,10))  
 new_speeds  
  
 Prediction of new data  
 predict(lin_mod,newdata = new_speeds)  
  confidence interval  
 predict(lin_mod,newdata = new_speeds,interval = "confidence")  
 predict(lin_mod,newdata = new_speeds,interval="prediction")  
  Visualizing Confidence and Prediction interval  
 pred_int = predict(lin_mod,interval='prediction')  
 mydata =cbind(cars,pred_int)  
 mydata  
  cbind= column bind - it joins objects column -wise  
 Regression line +_ Confidence interval  
 library("ggplot2")  
 p = ggplot(mydata,aes(speed,dist))+geom_point()+stat_smooth(method=lm)  
 p 
 Adding prediction intervals  
 p+geom_line(aes(y=lwr),color='purple',linetype="dashed")+  
   geom_line(aes(y=upr),color='green',linetype="dashed")  
  p = exsting ggplot object:= - add more layers  
  geom_line(0 = conects obs with a line  
 inbu8  
 stackloss  
 stackloss_lm = lm(stack.loss~Air.Flow+Water.Temp+Acid.Conc.,data=stackloss)  
 stackloss_lm  
 newdata = data.frame(Air.Flow=c(72,82,69,77),  
                      Water.Temp = c(20,25,18,22),  
                      Acid.Conc. = c(85,90,88,92))  
 newdat a 
 predict(stackloss_lm,newdata = newdata)  
 predict(stackloss_lm,newdata = newdata,interval = "confidence")  
 predict(stackloss_lm,newdata = newdata,interval="prediction")  
 pred2_int = predict(stackloss_lm,interval='prediction')  
 mydata =cbind(stackloss,pred2_int)  
 mydata  
 Regression line +_ Confidence interval  
 library("ggplot2")  
 p = ggplot(mydata,aes(Water.Temp,Acid.Conc.))+geom_point()+stat_smooth(method=lm)  
 p 



 EXP-6:-Multiple regression - estimation of paramters , fitting of the model , error ana lysis , model 
 validation , variable selection and testing  


 data(mtcars)  
 model=lm(mpg~cyl+disp+hp+drat+wt+qsec+vs+am+gear+carb,data = mtcars)  
 model  
 summary(model)  
 teststat=coef(summary(model))[3,1]/coef(summary(model))[3,2]  
 teststat  
 2*pt(teststat,21,lower.tail = F)  
 teststat1=coef(summary(model))[1,1]/coef(summary(model))[1,2]  
 teststat1  
 residuals=model$residuals  
 hist(residuals)  
 qqnorm(residuals)  
 qqline(residuals)  
 plot(model$residuals~mtcars$disp)  
 abline(0,0)  
 plot(model)  
 model1=lm(mpg~cyl+log(disp)+log(hp)+drat+wt+qsec+vs+am+gear+carb,data=mtcars)  
 summary(model1)  
 plot(model1)  
 library(MASS)  
 stepAIC(model)  
 model2=lm(mpg~qsec+wt+am,data=mtcars)  
 summary(model2)  
 model3=lm(mpg~log(disp)+gear+carb,data=mtcars)  
 summary(model3)  
 model4=lm(mpg~qsec+wt*am,data=mtcars)  
 summary(model4)  
 AIC(model4)  
 new_values=data.frame(wt=2.92,qsec=20.1,am=1)  
 new_values  
 pred_y=predict(model2,new_values,interval='predict')  
 pred_y  
 conf_y=predict(model2,new_values,interval='confidence')  
 conf_y  


 EXP-7:-proble m of multicollinearity  and problem of VIF 

 
 library('tidyverse')  
 mydata=mtcars%>%select(mpg,cyl,disp,hp,wt)  
 head(mydata)  
 model=lm(mpg~.,data = mydata)  
 model  
 library('corrplot')  
 corrplot(cor(mydata),method='number')  
 library(olsrr)  
 ols_vif_tol(model)  
 ols_eigen_cindex(model)  


'''