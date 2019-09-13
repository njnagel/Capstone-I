   ![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/485px-2016_Presidential_Election_by_Vote_Distribution_Among_States.svg.png)
   
   
   
   

# Population Characteristics of the 2016 Presidential Voters

The 2016 presidential election has highlighted a division in the US population. At the same time, the country faces one of the largest public health crises ever. The opioid epidemic is responsible for the longest sustained decline in U.S. life expectancy since the time of World War I and the Great Influenza. In 2017, nearly 50,000 Americans died from an opioid overdose - with an estimated 2 million more living with opioid addiction every day. This project is intended to understand more about these populations.

The data used for this project included multiple datasets from 2017 consisting of opioid deaths, social indicators,election results, and populations.

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
 
DATA PREP
  
The datasets were merged on state name to produce the analytic data slab. 

  - States were categorized according to which presidential candidate recieved the most popular votes.
  - Rates of overdose deaths were computed using state population totals to get a per 1000 rate
  - Death counts under a certain numer cannot be reported per HIPAA, so those totals, identified as "not reported" used a value of zero

DATA ANALYSIS

Initial descriptives were performed on the data, with distirbutions of the measures below:

![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/vardists.png)


The opiate overdose death rates for all states are presented separately.

![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/HeroinbyState.png)

![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/MethbyState.png)

![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/SynthbyState.png)

![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/NatSemibyState.png)


Exploratory analysis of the data showed possible relationships between some of the factors, evident in the matrix of scatter plots.


![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/scattermatrixreducednum.png)




Pairwise correlations show a range of correlations from negative to positive. Correlations are presented in the heatmap below, with positive values in red and negative in shades of blue.



![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/corrheatmapwnums.png)


The corresponding p-values reflect the probability of observing a value as extreme or more extreme, under the null hypthesis that the correlation is zero. 


![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/corrheatmapwpvalues.png)


The figure shows interesting results related to Uninsured Rate, with significant negative correlations. 

![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/Uninsrateopiates.png)


HYPOTHESIS TESTING

Question: Do the populations that voted for the two main candidates differ in opiate deaths?

1.  Heroin Rate T = .036, Heroin Rate C = .0062

    Null Hypothesis: Heroin Rates of Death are equal for T voters and C voters
    
    Alternative Hypothesis: Heroin Rates of Death are different for the two groups
    
    alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
    
    Test to use - z-test for proportions
    
    Test statistic = 2.73, p = .0087
    
    Decision: reject the null hypothesis in favor of the alternative
    
2. Methadone Rate T = .0067, Methadone Rate C = .017


    Null Hypothesis: Methadone Rates of Death are equal for T voters and C voters
    
    Alternative Hypothesis: Methadone Rates of Death are different for the two groups
    
    alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
    
    Test to use - z-test for proportions
    
    Test statistic = 4.68, p = .0000029
    
    Decision: reject the null hypothesis in favor of the alternative
    
3. Synthetic Rate T = .074, Synthetic Rate C = .127    


    Null Hypothesis: Synthetic Opioid Rates of Death are equal for T voters and C voters
    
    Alternative Hypothesis: Synthetic Opioid Rates of Death are different for the two groups
    
    alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
    
    Test to use - z-test for proportions
    
    Test statistic = 2.08, p = .040
    
    Decision: Fail to reject the null hypothesis in favor of the alternative
    
4. Natural, SemiSynthetic Rate T = .050, Natural, SemiSynthetic Rate C = .049 


    Null Hypothesis: Natural, SemiSynthetic Rates of Death are equal for T voters and C voters
    
    Alternative Hypothesis: Natural, SemiSynthetic Rates of Death are different for the two groups
    
    alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
    
    Test to use - z-test for proportions
    
    Test statistic = .185, p = .85
    
    Decision: Fail to reject the null hypothesis in favor of the alternative
  
Question: Do the popoulations that voted for each of the candidates differ on social health indicators?

1. Uninsured Rate T = .13, Uninsured Rate C = .09

  Null Hypothesis: Uninsured Rates don't differ between the two groups
  
  Alternative Hypothesis: Uninsured Rates do differ between the two groups
  
  alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
  
  Test to use - z-test for proportions
  
  Test statistic = 3.92, p = .000008
  
  Decision: Reject the null hypothesis in favor of the alternative
  
2. Poverty Rate T = .30, Poverty Rate C = .24

  Null Hypothesis: Poverty Rates don't differ between the two groups
  
  Alternative Hypothesis: Poverty Rates do differ between the two groups
  
  alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
  
  Test to use - z-test for proportions
  
  Test statistic = 4.70, p = .0000026
  
  Decision: Reject the null hypothesis in favor of the alternative  
  
3. Urban Rate T = 81, Urban Rate C = 69

  Null Hypothesis: Urban Population Rates don't differ between the two groups
  
  Alternative Hypothesis: Urban Population Rates do differ between the two groups
  
  alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
  
  Test to use - z-test for proportions
  
  Test statistic = 3.09, p = .0020
  
  Decision: Reject the null hypothesis in favor of the alternative  
  
4. Immunization Rate T = .71, Immunization Rate C = .73

  Null Hypothesis: Immunization Rates don't differ between the two groups
  
  Alternative Hypothesis: Immunization Rates do differ between the two groups
  
  alpha = .05? NO! multiple comparisons, so alpha = .05/4 = .0125
  
  Test to use - z-test for proportions
  
  Test statistic = 2.24, p = .025
  
  Decision: Fail to reject the null hypothesis in favor of the alternative  
  
  LOGISTIC REGRESSION ANALYSIS
  
  We are modeling the binary outcome of election result using 0 and 1's. Independent variables include the eight rates.
  
  The resulting Accuracy measure is .77.
  
  The confusion matrix that reflects the assignment of the training data set is below:
  
  ![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/confusionmatrixlogreg.png)
  
  The level of accuracy is good, with 10 of 13 training cases being classified correctly.


