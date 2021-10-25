import pandas as pd
import numpy as np
import seaborn as sns

def connecting_unprocessed(excel_file):
    '''Taking excel spreadsheet and converting to .csv format'''
    #Reading each sheet from the excel file
    df1 = pd.read_excel(excel_file, sheet_name='PUF_2006', header=1)
    df2 = pd.read_excel(excel_file, sheet_name='PUF_2007', header=1)
    df3 = pd.read_excel(excel_file, sheet_name='PUF_2008', header=1)
    df4 = pd.read_excel(excel_file, sheet_name='PUF_2009', header=1)
    df5 = pd.read_excel(excel_file, sheet_name='PUF_2010', header=1)
    df6 = pd.read_excel(excel_file, sheet_name='PUF_2011', header=1)
    df7 = pd.read_excel(excel_file, sheet_name='PUF_2012', header=1)
    
    #Add the sheet year as a column to each df
    df1['Year'] = 2006
    df2['Year'] = 2007
    df3['Year'] = 2008
    df4['Year'] = 2009
    df5['Year'] = 2010
    df6['Year'] = 2011
    df7['Year'] = 2012
    
    #Concatenating dfs
    frames = [df1, df2, df3, df4, df5, df6, df7]
    data = pd.concat(frames)
    
    #Reorganizing column order
    cols = list(data.columns)
    cols = [cols[-1]] + cols [:-1]
    df = data[cols]
    
    df.to_csv('../data/raw/data.csv', sep=',', index=False)
    return df

def unprocessed(csv_file):
    df = pd.read_csv(csv_file)
    return df

def rename_data(df):
    df1 = df.rename(columns={"Percent of people who have had a heart attack" : "ha%",
                            "Percent of people with atrial fibrillation" : "af%",
                            "Percent of people with heart failure" : "hf%",
                            "Percent of people with diabetes" : "dm%",
                            "Percent of people with high cholesterol" : "hc%",
                            "Percent of people with hypertension" : "hyp%",
                            "Percent of people with ischemic heart disease" : "ihd%",
                            "Percent of people with stroke or TIA" : "strokeorTIA%",
                            "Percent of people with obesity" : "obesity%",
                            "Percent of people with peripheral vascular disease" : "pad%",
                            "Percent Female" : "F%",
                            "Percent Male" : "M%",
                            "Percent Non-Hispanic White" : "White%",
                            "Percent African American" : "AfrA%",
                            "Percent Hispanic" : "His%",
                            "Percent Asian or Pacific Islander" : "Asian%",
                            "Percent American Indian or Alaska Native" : "Indig%",
                            "Percent Other or Unknown Race" : "Unknown%",
                            "Percent under 40 Years" : "A%_<40",
                            "Percent between 40-64 Years" : "A%_40-64",
                            "Percent between 65-84 Years" : "A%_65-84",
                            "Percent 85+ Years" : "A%_85+"})
    return df1

def remove_columns(df):
    df1 = df[["Year",
              "State",
             "Region",
             "Number of People by Medicare-Medicaid Enrollment Type",
             "Number of People",
             "Number of People with FFS",
             "Number of Females with FFS",
             "Number of Males with FFS",
             "A%_<40",
             "A%_40-64",
             "A%_65-84",
             "A%_85+",
             "F%",
             "M%",
             "White%",
             "AfrA%",
             "His%",
             "Asian%",
             "Indig%",
             "Unknown%",
             "ha%",
             "af%",
             "hf%",
             "dm%",
             "hc%",
             "hyp%",
             "ihd%",
             "strokeorTIA%",
             "obesity%",
             "pad%",
             "Number of FFS people who used Medicare procedures",
             "Number of FFS people who used Medicare imaging services",
             "Number of FFS people who used Medicare laboratory/testing services",
             "Number of FFS people who used Medicare durable medical equipment",
             "Number of people who used Medicare Part D prescription drugs",
             "Total Medicare payments",
             "Total Medicare IP Hospital FFS payments",
             "Total Medicare Other IP Hospital FFS payments",
             "Total Medicare Part B drug FFS payments",
             "Total Medicare procedure FFS payments",
             "Total Medicare imaging FFS payments",
             "Total Medicare durable medical equipment FFS payments",
             "Total Medicare Part D prescription drug FFS costs (total RX cost)",
             "Number of FFS people who used Medicaid lab/xray services",
             "Number of FFS people who used Medicaid durable medical equipment services",
             "Number of FFS people who used Medicaid drugs",
             "Number of FFS people who used Medicaid clinic services",
             "Total Medicaid FFS payments", "Total Medicaid lab/xray FFS payments",
             "Total Medicaid durable medical equipment FFS payments",
             "Total Medicaid drug FFS payments",
             "Total Medicaid clinic payments"]]
    return df1

def add_region_column (df):
    '''Using State data to provide Region data'''
    #Midwest US Region
    df.loc[(df['State'] == 'ND') | (df['State'] == 'SD') | (df['State'] == 'NE') | (df['State'] == 'KS') | \
           (df['State'] == 'MN') | (df['State'] == 'IA') | (df['State'] == 'MO') | (df['State'] == 'WI') | \
           (df['State'] == 'IL') | (df['State'] == 'MI') | (df['State'] == 'IN') | (df['State'] == 'OH'), 'Region'] = 'Midwest'
    #Northeast US Region
    df.loc[(df['State'] == 'ME') | (df['State'] == 'DC') | (df['State'] == 'DE') | (df['State'] == 'VA') | \
           (df['State'] == 'NH') | (df['State'] == 'VT') | (df['State'] == 'MA') | (df['State'] == 'RI') | \
           (df['State'] == 'CT') | (df['State'] == 'NY') | (df['State'] == 'PA') | (df['State'] == 'NJ'), 'Region'] = 'Northeast'
    #Southeast US Region
    df.loc[(df['State'] == 'KY') | (df['State'] == 'LA') | (df['State'] == 'AR') | (df['State'] == 'TN') | \
           (df['State'] == 'MS') | (df['State'] == 'WV') | (df['State'] == 'NC') | (df['State'] == 'AL') | \
           (df['State'] == 'MD') | (df['State'] == 'SC') | (df['State'] == 'GA') | (df['State'] == 'FL'), 'Region'] = 'Southeast'
    #Southwest US Region
    df.loc[(df['State'] == 'AZ') | (df['State'] == 'NM') | (df['State'] == 'OK') | (df['State'] == 'TX'), 'Region'] = 'Southwest'
    #West US Region
    df.loc[(df['State'] == 'WA') | (df['State'] == 'OR') | (df['State'] == 'CA') | (df['State'] == 'HI') | \
           (df['State'] == 'AK') | (df['State'] == 'ID') | (df['State'] == 'NV') | (df['State'] == 'MT') | \
           (df['State'] == 'WY') | (df['State'] == 'UT') | (df['State'] == 'CO'), 'Region'] = 'West'
    #National
    df.loc[(df['State'] == 'National'), 'Region'] = 'NaN'
    return df

def missing_values (df):
    df1 = df.replace('*', 'NaN')
    df1 = df1.replace('.', 'NaN')
    return df1


#Data processing functions
def cleaned_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

