import numpy.random as nprand
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as mplt

import variableGenerator as vg
import causalMethods as cm

N = 500  # Number of data
repeat = 100  # How many times to try the causal analysis

# Formula
#   x = e_x
#   y = f(x, e_y)

# Random number generator for e_x, e_y
#   N: number of data point
def rand_for_e_x(N):
  return nprand.rand(N)*15.0-7.5  # uniform random number
  #return nprand.randn(N) # normal random number 

def rand_for_e_y(N):
  return nprand.rand(N)-0.5  # uniform random number 
  #return nprand.randn(N) # normal random number 

# Function to calculate Y from X and e_Y
def funcY(X, eY):
  ## Linear function example
  #   Y = 2X + 1 + eY
  #return vg.generate2ndVar(X, eY, vg.linearFunc, a=2, b=1) 

  # Polynomial function example
  #   Y = -0.05X^4 + 2X^3 + 3X^2 + 2X + 1
  #return vg.generate2ndVar(X, eY, vg.polynomialFunc, c=[-0.01, 0.25, 5, 2, 1])

  # Logistic funciton example
  #   Y = 1/(1+exp(-x))
  #return vg.generate2ndVar(X, eY, vg.logisticFunc, a=0, b=1, c=1, d=0)

  # PNL model  Y = f1(f2(x) + e_y)
  return np.sin(0.05 * vg.generate2ndVar(X, eY, vg.polynomialFunc, c=[-0.01,0.25,5,2,1]))



def repeatCausalPair(N, repeat):
  print("CORRECT DIRECTION: X->Y")
  ANMcount = 0
  IGCIcount = 0
  LINGAMcount = 0
  for i in range(repeat):
    X  = rand_for_e_x(N)  # X (= error varialbe for X, e_x)
    eY = rand_for_e_y(N)  # error variable for Y, e_y

    Y = funcY(X, eY)

    # Write X-Y plot in the first loop
    if i == 0:
      mplt.figure()
      mplt.scatter(X, Y)
      mplt.savefig('XYplot.png')

    anm, igci = cm.methodANM_IGCI(X,Y)
    ANMcount += anm
    IGCIcount += igci

    LINGAMcount += cm.methodLiNGAM(X,Y)

    if i%10 == 0:
      print(".", end="", flush=True)
 
  return(ANMcount, IGCIcount, LINGAMcount)


counts = repeatCausalPair(N, repeat)
print()
print("Ratio of correct answer X->Y ")
print(counts[0]/repeat, " for ANM")
print(counts[1]/repeat, " for IGCI")
print(counts[2]/repeat, " for LiNGAM")

