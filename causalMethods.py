from cdt.causality.pairwise import (ANM, IGCI)
from cdt.utils.io import read_causal_pairs
import lingam as lg

from sklearn.preprocessing import scale as scaler
import pandas as pd
import numpy as np

# return value: (resultANM, resultIGCI) 
#   value: 1 (correct) for X->Y, 0 (not correct) for Y->X
def methodANM_IGCI(X, Y):
  answerANM = 0
  answerIGCI = 0
  data = pd.Series({"X":scaler(X), "Y":scaler(Y)})

  m = ANM()
  pred = m.predict(data)
  #print(pred, "(ANM, Value : 1 if X->Y and -1 if Y->X)")
  if(pred > 0):
    answerANM=1

  m = IGCI()
  pred = m.predict(data)
  #print(pred[0], "(IGCI, Value: >0 if X->Y and <0 if Y->X)")
  if(pred > 0):
    answerIGCI+=1  

  return answerANM, answerIGCI

# return value: 1 (correct) for X->Y, 0 (not correct) for Y->X
def methodLiNGAM(X, Y):
  data = np.c_[X,Y]
  lingamPred = lg.estimate(data)
  #print(lingamPred)
  if(lingamPred[0,1] == 0):
    #print("LiNGAM is correct")
    return 1
  else:
    #print("LiNGAM is wrong")
    return 0

