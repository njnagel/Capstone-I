

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

  - States were categorized according to which presidential candidate recieved the most popular votes.
  - Rates of overdose deaths were computed using state population totals to get a per 1000 rate
  - Death counts under a certain numer cannot be reported per HIPAA, so those totals, identified as "not reported" used a value of zero

DATA ANALYSIS

Initial descriptives were performed on the data, with distirbutions of the measures below:

![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/vardists.png)

Exploratory analysis of the data showed possible relationships between some of the factors, evident in the matrix of scatter plots.


![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/scattermatrixreducednum.png)




Pairwise correlations show a range of correlations from negative to positive. Correlations are presented in the heatmap below, with positive values in red and negative in shades of blue.



![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/corrheatmapwnums.png)


The corresponding p-values reflect the probability of observing a value as extreme or more extreme, under the null hypthesis that the correlation is zero. 


![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/corrheatmapwpvalues.png)


HYPOTHESIS TESTING

Question: Do the populations that voted for the two main candidates differ in opiate deaths?

1.  Heroin Rate T = .036, Heroin Rate C = .066

    Null Hypothesis: Heroin Rates of Death are equal for T voters and C voters
    
    Alternative Hypothesis: Heroin Rates of Death are different for the two groups
    
    alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
    
    Test to use - t-test for two samples
    
    Test statistic = 2.73, p = .0087
    
    Decision: reject the null hypothesis in favor of the alternative
    
2. Methadone Rate T = .0067, Methadone Rate C = .017


    Null Hypothesis: Methadone Rates of Death are equal for T voters and C voters
    
    Alternative Hypothesis: Methadone Rates of Death are different for the two groups
    
    alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
    
    Test to use - t-test for two samples
    
    Test statistic = 4.68, p = .000024
    
    Decision: reject the null hypothesis in favor of the alternative
    
3. Synthetic Rate T = .074, Synthetic Rate C = .127    


    Null Hypothesis: Synthetic Opioid Rates of Death are equal for T voters and C voters
    
    Alternative Hypothesis: Synthetic Opioid Rates of Death are different for the two groups
    
    alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
    
    Test to use - t-test for two samples
    
    Test statistic = 2.08, p = .042
    
    Decision: Fail to reject the null hypothesis in favor of the alternative
    
4. Natural, SemiSynthetic Rate T = .050, Natural, SemiSynthetic Rate C = .049 


    Null Hypothesis: Natural, SemiSynthetic Rates of Death are equal for T voters and C voters
    
    Alternative Hypothesis: Natural, SemiSynthetic Rates of Death are different for the two groups
    
    alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
    
    Test to use - t-test for two samples
    
    Test statistic = .185, p = .85
    
    Decision: Fail to reject the null hypothesis in favor of the alternative
  
Question: Do the popoulations that voted for each of the candidates differ on social health indicators?

1. Uninsured Rate T = .13, Uninsured Rate C = .09

  Null Hypothesis: Uninsured Rates don't differ between the two groups
  
  Alternative Hypothesis: Uninsured Rates do differ between the two groups
  
  alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
  
  Test to use - t-test for two samples
  
  Test statistic = 3.92, p = .00028
  
  Decision: Reject the null hypothesis in favor of the alternative
  
2. Poverty Rate T = .30, Poverty Rate C = .24

  Null Hypothesis: Poverty Rates don't differ between the two groups
  
  Alternative Hypothesis: Poverty Rates do differ between the two groups
  
  alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
  
  Test to use - t-test for two samples
  
  Test statistic = 4.70, p = .000022
  
  Decision: Reject the null hypothesis in favor of the alternative  
  
3. Urban Rate T = 81, Urban Rate C = 69

  Null Hypothesis: Urban Population Rates don't differ between the two groups
  
  Alternative Hypothesis: Urban Population Rates do differ between the two groups
  
  alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
  
  Test to use - t-test for two samples
  
  Test statistic = 3.09, p = .0033
  
  Decision: Reject the null hypothesis in favor of the alternative  
  
4. Immunization Rate T = .30, Immunization Rate C = .24

  Null Hypothesis: Immunization Rates don't differ between the two groups
  
  Alternative Hypothesis: Immunization Rates do differ between the two groups
  
  alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
  
  Test to use - t-test for two samples
  
  Test statistic = 2.24, p = .030
  
  Decision: Fail to reject the null hypothesis in favor of the alternative  

winner
C    0.7308
T    0.7055
Name: Perc_Immun, dtype: float64
Ttest_indResult(statistic=-2.238827559482427, pvalue=0.02983878793839024)

