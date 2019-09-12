

# Capstone-I

The opioid epidemic is responsible for the longest sustained decline in U.S. life expectancy since the time of World War I and the Great Influenza. In 2017, nearly 50,000 Americans died from an opioid overdose - with an estimated 2 million more living with opioid addiction every day. This project is intended to understand more about this population.

The data used for this project included multiple datasets from 2017 consisting of opioid deaths, social indicators,electionn results, and populations.

The datasets included:
  - Counts of different types of opioid deaths for each state 
      
      Synthetic Opioids
      
      Natural, Semisynthetic 
      
      Methadone 
      
      Heroin
      
  - State populations 
  - Rates of uninsured 
  - Rates of immunization
  - Poverty rates 
  - Urban population
  - Popular vote counts for the 2016 presidential election
  
The datasets were merged on state name to produce the analytic data slab.  

Initial descriptives were performed on the data, with distirbutions of the measures below:

![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/vardists.png)

Exploratory analysis of the data showed possible relationships between some of the factors, evident in the matrix of scatter plots.


![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/scattermatrixreducednum.png)



Pairwise correlations show a range of correlations from negative to positive. Correlations are presented in the heatmap below, with positive values in red and negative in shades of blue.



![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/corrheatmapwnums.png)


The corresponding p-values reflect the probability of observing a value as extreme or more extreme, under the null hypthesis that the correlation is zero. 


![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/corrheatmapwpvalues.png)



  analysisdata['winner'][i] = 'T' if analysisdata['PV_Trump'][i] > analysisdata['PV_Clinton'][i] else 'C'
winner
C    0.065593
T    0.035923
Name: HeroinRate, dtype: float64
Ttest_indResult(statistic=-2.7372999654234773, pvalue=0.0086618666053406)
winner
C    0.016529
T    0.006650
Name: MethRate, dtype: float64
Ttest_indResult(statistic=-4.678277417250803, pvalue=2.388806761336747e-05)
winner
C    0.126917
T    0.074349
Name: SynthRate, dtype: float64
Ttest_indResult(statistic=-2.0847773866193666, pvalue=0.04243297966655116)
winner
C    0.048752
T    0.050103
Name: NatSemiRate, dtype: float64
Ttest_indResult(statistic=0.18594481457428477, pvalue=0.8532716261483074)
winner
C    0.087500
T    0.132667
Name: TotalUninsRate, dtype: float64
Ttest_indResult(statistic=3.9227585968090746, pvalue=0.0002780926479508915)
winner
C    0.236500
T    0.300667
Name: Under_200%, dtype: float64
Ttest_indResult(statistic=4.698230853014776, pvalue=2.2345081254552617e-05)
winner
C    81.390000
T    69.023333
Name: PercUrban, dtype: float64
Ttest_indResult(statistic=-3.095159479837517, pvalue=0.003278439319152115)
winner
C    0.7308
T    0.7055
Name: Perc_Immun, dtype: float64
Ttest_indResult(statistic=-2.238827559482427, pvalue=0.02983878793839024)

