import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os
import seaborn as sns
import scipy.stats as sc
from scipy.stats import pearsonr


state_ods = pd.read_csv('../../../Downloads/raw_data.csv', sep = ',')
election = pd.read_excel('../../../Downloads/2016Election5.xlsx')
statepops = pd.read_excel('../../../Downloads/state_pops.xlsx')
uninsured = pd.read_csv('../../../Downloads/uninsuredrates.csv')
immundat = pd.read_csv('../../../Downloads/immun.csv')
fpldat = pd.read_csv('../../../Downloads/fpl.csv')
urbandat = pd.read_excel('../../../Downloads/urbanperc.xlsx')
pd.set_option('display.max_columns', None)

#OD data below certain levels can't be reported
state_ods = state_ods.replace('NSD', 0)

#getting data types
fpldat.Location = fpldat.Location.astype(str)
state_ods['Synthetic'] = state_ods['Synthetic'].astype(float)
state_ods.Methadone = state_ods.Methadone.astype(float)
state_ods.Heroin = state_ods.Heroin.astype(float)

#Merging data files on Location (state)
drug_election = state_ods.merge(election, on = 'Location')
drug_election_pops = drug_election.merge(statepops, on = 'Location')
drug_elec_pop_unins = drug_election_pops.merge(uninsured, on = 'Location')
drug_elec_pop_unins_fpl = drug_elec_pop_unins.merge(fpldat, on = 'Location')
drug_elec_pop_unins_fpl_urb = drug_elec_pop_unins_fpl.merge(urbandat, on = 'Location')
analysisdata = drug_elec_pop_unins_fpl_urb.merge(immundat, on = 'Location')

#Creating field to contain winner of the popular vote in each state
analysisdata['winner'] = 'C'
i = 0
for item in analysisdata['winner']:
    analysisdata['winner'][i] = 'T' if analysisdata['PV_Trump'][i] > analysisdata['PV_Clinton'][i] else 'C'
    i = i + 1   

#Tranforming counts into rates
analysisdata['NatSemiRate'] = 1000*((analysisdata['NaturalSemisynthetic'])/analysisdata['StatePop'])    
analysisdata['SynthRate'] = 1000*((analysisdata['Synthetic'])/analysisdata['StatePop'])
analysisdata['MethRate'] = 1000*((analysisdata['Methadone'])/analysisdata['StatePop'])
analysisdata['HeroinRate'] = 1000*((analysisdata['Heroin'])/analysisdata['StatePop'])

#I don't know why i get the error but this solves it
analysisdata.HeroinRate = analysisdata.HeroinRate.astype(float)

#Getting measures for comparison
TrumpdataHer = analysisdata.loc[analysisdata['winner'] == 'T'].dropna()['HeroinRate']
ClintondataHer = analysisdata.loc[analysisdata['winner'] == 'C'].dropna()['HeroinRate']
TrumpdataMeth = analysisdata.loc[analysisdata['winner'] == 'T'].dropna()['MethRate']
ClintondataMeth = analysisdata.loc[analysisdata['winner'] == 'C'].dropna()['MethRate']
TrumpdataSynth = analysisdata.loc[analysisdata['winner'] == 'T'].dropna()['SynthRate']
ClintondataSynth = analysisdata.loc[analysisdata['winner'] == 'C'].dropna()['SynthRate']
TrumpdataNatsemi = analysisdata.loc[analysisdata['winner'] == 'T'].dropna()['NatSemiRate']
ClintondataNatsemi = analysisdata.loc[analysisdata['winner'] == 'C'].dropna()['NatSemiRate']


#Get means 
Hermeans = analysisdata.groupby('winner')['HeroinRate'].mean()
Synthmeans = analysisdata.groupby('winner')['SynthRate'].mean()
Semimeans = analysisdata.groupby('winner')['NatSemiRate'].mean()
Methmeans = analysisdata.groupby('winner')['MethRate'].mean()


print(Hermeans)
sigtest1 = sc.ttest_ind(TrumpdataHer, ClintondataHer)
print(sigtest1)
print(Methmeans)
sigtest2 = sc.ttest_ind(TrumpdataMeth, ClintondataMeth)
print(sigtest2)
print(Synthmeans)  
sigtest3 = sc.ttest_ind(TrumpdataSynth, ClintondataSynth) 
print(sigtest3)
print(Semimeans)
sigtest4 = sc.ttest_ind(TrumpdataNatsemi, ClintondataNatsemi)
print(sigtest4)



analysisdata2 = analysisdata[['winner', 'HeroinRate','SynthRate','NatSemiRate','MethRate', 'TotalUninsRate','Under_200%','PercUrban','Perc_Immun']].copy()
analysisdata3 = analysisdata2[['HeroinRate','SynthRate','NatSemiRate','MethRate', 'TotalUninsRate','Under_200%','PercUrban','Perc_Immun']].copy()
Trumpdata = analysisdata2.loc[analysisdata2['winner'] == 'T']
Clintondata = analysisdata2.loc[analysisdata2['winner'] == 'C']


corr = analysisdata2.corr()
#print(analysisdata2.corr())

#get pvalues for correlations
   
df_corr = pd.DataFrame() # Correlation matrix
df_p = pd.DataFrame()  # Matrix of p-values
for x in analysisdata3.columns:
    for y in analysisdata3.columns:
        correl = sc.pearsonr(analysisdata3[x], analysisdata3[y])
        df_corr.loc[x,y] = correl[0]
        df_p.loc[x,y] = correl[1]
#print(df_corr)
#print(df_p)   

            

#some plotting
#corr.style.background_gradient(cmap='coolwarm', axis = None).set_precision = 2

#fig, ax = plt.subplots(figsize=(10, 10))
#ax.matshow(corr)
#plt.xticks(range(len(corr.columns)), corr.columns);
#plt.yticks(range(len(corr.columns)), corr.columns);

f, ax = plt.subplots(figsize=(10, 8))
corr = analysisdata2.corr()
#sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), annot = True, cmap=sns.diverging_palette(220, 10, as_cmap=True),
#            square=True, ax=ax)


sns.heatmap(df_p, mask=np.zeros_like(df_p, dtype=np.bool), annot = True, annot_kws = {'size' : 8}, cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)            

sm = pd.plotting.scatter_matrix(analysisdata2, alpha=0.2, figsize=(60, 60))
#Change label rotation
[s.xaxis.label.set_rotation(45) for s in sm.reshape(-1)]
[s.yaxis.label.set_rotation(0) for s in sm.reshape(-1)]

#May need to offset label when rotating to prevent overlap of figure
[s.get_yaxis().set_label_coords(-0.3,0.5) for s in sm.reshape(-1)]

#Hide all ticks
[s.set_xticks(()) for s in sm.reshape(-1)]
[s.set_yticks(()) for s in sm.reshape(-1)]


plt.show()

#engine = create_engine('postgresql://'+os.environ['POSTGRESQL_USER']+':'+os.environ['POSTGRESQL_PASSWORD']+'@'+os.environ['POSTGRESQL_HOST_IP']+':'+os.environ['POSTGRESQL_PORT']+'/'+os.environ['POSTGRESQL_DATABASE'],echo=False)
#engine = create_engine('postgresql+psycopg2://njnagel: password@0.0.0.0:8881/opiatesanalysis')
#analysisdata.to_sql(name='Opiates', con=engine, if_exists = 'replace', index=False)

#calculate_pvalues(analysisdata2)
       