import pandas as pd


#Please place the input file in current working directory from where you will execute this code.

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Read in your .csv files as dataframes using pd.read_csv()
df_log1 = pd.read_csv("Jmeter_log1.jtl")
df_log2 = pd.read_csv("Jmeter_log2.jtl")
# This method combines a list of pandas dataframes into one dataframe
f = pd.concat([df_log1, df_log2])

#If you want to display each and every column of both CSV just uncomment the below cdde

#print(f)

print(f.columns)

#Convert timestamp in PST TimeZone

f['timeStamp'] = pd.to_datetime(f['timeStamp'],unit='ms').dt.tz_localize('UTC').dt.tz_convert('US/Pacific')

f['timeStamp'] = f['timeStamp'].dt.strftime('%Y-%m-%d %H:%M:%S %Z')

print(f['timeStamp'])

#Applied the condition to display only those results which do not have responseCode of 200

rslt_df = f[f['responseCode'] != 200]

#Filling NAN values
rslt_df.fillna('',inplace=True)

#Resultant Output
print(rslt_df[['label','responseCode','responseMessage','failureMessage','timeStamp']])