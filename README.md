# Capstone-I

The data used for this project included counts of different types of opioid deaths for each state, state populations, rates of uninsured, rates of immunization, poverty rates, and extent of urban population for each state.

                      NaturalSemisynthetic  Synthetic  Methadone    Heroin  \
NaturalSemisynthetic              1.000000   0.763440   0.831755  0.799890   
Synthetic                         0.763440   1.000000   0.635754  0.833968   
Methadone                         0.831755   0.635754   1.000000  0.802421   
Heroin                            0.799890   0.833968   0.802421  1.000000   
PV_Trump                          0.888197   0.604612   0.725870  0.724222   
PV_Clinton                        0.835727   0.535378   0.838044  0.737354   
StatePop                          0.828273   0.467812   0.786451  0.681755   
MaleUninsRate                     0.132857  -0.191303  -0.045186 -0.123295   
FemaleUninsRate                   0.115766  -0.199643  -0.062683 -0.127816   
TotalUninsRate                    0.114179  -0.203188  -0.066440 -0.134676   
Under_200%                        0.129196  -0.083554  -0.106824 -0.090188   
200%+                            -0.135070   0.079492   0.103827  0.089796   
Total                                  NaN        NaN        NaN       NaN   
PercUrban                         0.393905   0.291003   0.492260  0.450579   
Perc_Immun                       -0.160125   0.027313  -0.078176 -0.084078   
NatSemiRate                       0.194168   0.200177   0.072622  0.059706   
SynthRate                         0.183686   0.546117   0.188305  0.307225   
MethRate                          0.069590   0.164260   0.332915  0.134624   
HeroinRate                        0.187915   0.394477   0.254901  0.441135   

                      PV_Trump  PV_Clinton  StatePop  MaleUninsRate  \
NaturalSemisynthetic  0.888197    0.835727  0.828273       0.132857   
Synthetic             0.604612    0.535378  0.467812      -0.191303   
Methadone             0.725870    0.838044  0.786451      -0.045186   
Heroin                0.724222    0.737354  0.681755      -0.123295   
PV_Trump              1.000000    0.889510  0.935097       0.243290   
PV_Clinton            0.889510    1.000000  0.970829       0.042821   
StatePop              0.935097    0.970829  1.000000       0.183146   
MaleUninsRate         0.243290    0.042821  0.183146       1.000000   
FemaleUninsRate       0.261105    0.048218  0.196164       0.967925   
TotalUninsRate        0.245387    0.032556  0.181167       0.991510   
Under_200%            0.164310   -0.027044  0.083828       0.555026   
200%+                -0.168220    0.024323 -0.086885      -0.558034   
Total                      NaN         NaN       NaN            NaN   
PercUrban             0.341365    0.449216  0.409566      -0.134350   
Perc_Immun           -0.226713   -0.146024 -0.213081      -0.313260   
NatSemiRate          -0.127569   -0.174345 -0.173835      -0.038059   
SynthRate            -0.017179    0.000579 -0.070492      -0.457199   
MethRate             -0.147731   -0.026592 -0.093374      -0.378337   
HeroinRate            0.011469    0.066177 -0.002929      -0.367464   

                      FemaleUninsRate  TotalUninsRate  Under_200%     200%+  \
NaturalSemisynthetic         0.115766        0.114179    0.129196 -0.135070   
Synthetic                   -0.199643       -0.203188   -0.083554  0.079492   
Methadone                   -0.062683       -0.066440   -0.106824  0.103827   
Heroin                      -0.127816       -0.134676   -0.090188  0.089796   
PV_Trump                     0.261105        0.245387    0.164310 -0.168220   
PV_Clinton                   0.048218        0.032556   -0.027044  0.024323   
StatePop                     0.196164        0.181167    0.083828 -0.086885   
MaleUninsRate                0.967925        0.991510    0.555026 -0.558034   
FemaleUninsRate              1.000000        0.986742    0.516384 -0.517437   
TotalUninsRate               0.986742        1.000000    0.542675 -0.544155   
Under_200%                   0.516384        0.542675    1.000000 -0.998841   
200%+                       -0.517437       -0.544155   -0.998841  1.000000   
Total                             NaN             NaN         NaN       NaN   
PercUrban                   -0.155820       -0.154388   -0.326808  0.332722   
Perc_Immun                  -0.334147       -0.312920   -0.344655  0.352822   
NatSemiRate                 -0.118970       -0.069142    0.183653 -0.189741   
SynthRate                   -0.497009       -0.467729   -0.218248  0.214514   
MethRate                    -0.421963       -0.400352   -0.224100  0.224712   
HeroinRate                  -0.444290       -0.406079   -0.133579  0.126111   

                      Total  PercUrban  Perc_Immun  NatSemiRate  SynthRate  \
NaturalSemisynthetic    NaN   0.393905   -0.160125     0.194168   0.183686   
Synthetic               NaN   0.291003    0.027313     0.200177   0.546117   
Methadone               NaN   0.492260   -0.078176     0.072622   0.188305   
Heroin                  NaN   0.450579   -0.084078     0.059706   0.307225   
PV_Trump                NaN   0.341365   -0.226713    -0.127569  -0.017179   
PV_Clinton              NaN   0.449216   -0.146024    -0.174345   0.000579   
StatePop                NaN   0.409566   -0.213081    -0.173835  -0.070492   
MaleUninsRate           NaN  -0.134350   -0.313260    -0.038059  -0.457199   
FemaleUninsRate         NaN  -0.155820   -0.334147    -0.118970  -0.497009   
TotalUninsRate          NaN  -0.154388   -0.312920    -0.069142  -0.467729   
Under_200%              NaN  -0.326808   -0.344655     0.183653  -0.218248   
200%+                   NaN   0.332722    0.352822    -0.189741   0.214514   
Total                   NaN        NaN         NaN          NaN        NaN   
PercUrban               NaN   1.000000   -0.012206    -0.018108   0.021297   
Perc_Immun              NaN  -0.012206    1.000000     0.081264   0.385709   
NatSemiRate             NaN  -0.018108    0.081264     1.000000   0.558146   
SynthRate               NaN   0.021297    0.385709     0.558146   1.000000   
MethRate                NaN   0.260658    0.241416     0.504202   0.628870   
HeroinRate              NaN   0.287147    0.202766     0.513006   0.709745   

                      MethRate  HeroinRate  
NaturalSemisynthetic  0.069590    0.187915  
Synthetic             0.164260    0.394477  
Methadone             0.332915    0.254901  
Heroin                0.134624    0.441135  
PV_Trump             -0.147731    0.011469  
PV_Clinton           -0.026592    0.066177  
StatePop             -0.093374   -0.002929  
MaleUninsRate        -0.378337   -0.367464  
FemaleUninsRate      -0.421963   -0.444290  
TotalUninsRate       -0.400352   -0.406079  
Under_200%           -0.224100   -0.133579  
200%+                 0.224712    0.126111  
Total                      NaN         NaN  
PercUrban             0.260658    0.287147  
Perc_Immun            0.241416    0.202766  
NatSemiRate           0.504202    0.513006  
SynthRate             0.628870    0.709745  
MethRate              1.000000    0.646351  
HeroinRate            0.646351    1.000000

![alt text](https://github.com/njnagel/Capstone-I/blob/master/img/scattermatrixreducednum.png)
