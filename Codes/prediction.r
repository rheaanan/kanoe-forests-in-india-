a = read.csv('lol2.csv')
ro = nrow(a)
start = 1
end = 7
h <- c()
hh <- c()
hhh <- c()

v <- c()
while(start <= ro)
{
  b = a[start:end,]
  
  t <- lm(Temp~Year, data = b)
  intert <- summary(t)$coefficients[1,1]
  cyt <- summary(t)$coefficients[2,1]
  x = intert + (cyt*2030)
  
  r <- lm(Rainfall~Year, data = b)
  intert1 <- summary(r)$coefficients[1,1]
  cyt1 <- summary(r)$coefficients[2,1]
  y = intert1 + (cyt1*2030)
  
  p <- lm(Pop~Year, data = b)
  intert2 <- summary(p)$coefficients[1,1]
  cyt2 <- summary(p)$coefficients[2,1]
  z = intert2 + (cyt2*2030)
  
  model <- lm(Forest~Temp+Pop+Rainfall, data = b)
  #print(summary(model))
  intert2 <- summary(model)$coefficients[1,1]
  cyt <- summary(model)$coefficients[2,1]
  cyp <- summary(model)$coefficients[3,1]
  cyr <- summary(model)$coefficients[4,1]
  e = intert2 + (cyt*x) + (cyp*z) + (cyr*y)
  
  #print(x)
  #print(y)
  #print(z)
  
  h <- c(h,x) #t
  hh <- c(hh,y) #r
  hhh <- c(hhh,z)  #p
  v <- c(v,e)
  start = start + 7
  end = end + 7
}
o <- a[c("District")]
oo <- unique(unlist(o))

print(oo)
q <- data.frame(oo,v,h,hh,hhh)
