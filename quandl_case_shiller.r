library(Quandl)
library(choroplethr)
# Quandl.auth(ENTER AUTH CODE)

## Getting data from Quandl ##

# example for how to read Quandl data to a df:
# df <- Quandl("FRED/AKSTHPI")

states <- state.abb
state_dfs <- list()

for (i in 1:length(state.abb))
{
  state = state.abb[i]
  print(state)
  q_code = paste0('FRED/', state, 'STHPI')
  state_dfs[[i]] = Quandl(q_code)
  state_dfs[[i]]$state = state
}

df <- data.frame(matrix(vector(), 0, 3, dimnames=list(c(), c("Date", "Value", "State"))), stringsAsFactors=F)

for (i in 1:length(state_dfs)) {
	df <- rbind(df, state_dfs[[i]])
}

## example choropleth ##

# latest date currently available in data is 2013-10-01
df_choro <- subset(df, df$Date == "2013-10-01")

colnames(df_choro)[2] <- "value"
colnames(df_choro)[3] <- "region"

choroplethr(df_choro, lod="state")


