import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import KFold

## Data Processing ##
def splitData(X, y, split_coeff):

    N, _ = X.shape # get the number of records 
    trainSize = int(split_coeff * N) # use the first split_coeff of the data as the training data

    XTrain = X[:trainSize] # the first training_size records
    yTrain = y[:trainSize]

    XTest = X[trainSize:] # the last test_size records
    yTest = y[trainSize:]

    return XTrain, yTrain, XTest, yTest

def extractSeason():
    return

def standardize(X):

    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    XStd = (X - mean)/std
    
    return XStd, mean, std

def basisExpansion(X, degree):
    
    poly = PolynomialFeatures(degree)
    xNew = poly.fit_transform(X)
    
    return xNew

# Convert relevant stats to Per/Game
def convertStatsToPG(X):
    #XTemp = X

    XTemp = X.select_dtypes(include=['float64'])
    XTemp = XTemp.apply(lambda col: col/X['Games Played'])
    #XTemp['Rank'] = X['Rank']

    # Replace all values with new per game values
    X['Goals'] = XTemp['Goals']
    X['Assists'] = XTemp['Assists']
    X['Points'] = XTemp['Points']
    X['Plus-Minus'] = XTemp['Plus-Minus']
    X['Penalty in Minutes'] = XTemp['Penalty in Minutes']
    X['Even Strength Goals'] = XTemp['Even Strength Goals']
    X['Even Strength Points'] = XTemp['Even Strength Points']
    X['Power Play Goals'] = XTemp['Power Play Goals']
    X['Power Play Points'] = XTemp['Power Play Points']
    X['Shorthanded Goals'] = XTemp['Shorthanded Goals']
    X['Shorthanded Points'] = XTemp['Shorthanded Points']
    X['Overtime Goals'] = XTemp['Overtime Goals']
    X['Game Winning Goals'] = XTemp['Game Winning Goals']
    X['Shots'] = XTemp['Shots']

    return X

def dataPrep(X, y, degree):

    validationRatio = 0.8
    trainingRatio = 0.8

    # Split data
    XTrain, yTrain, XTest, yTest = splitData(X, y, trainingRatio)

    # Standardize training data and do the same transformation to the test data
    standardizeXTrain = StandardScaler()
    XTrain = standardizeXTrain.fit_transform(XTrain)

    # Standardize test data using all X_train data
    XTest = standardizeXTrain.transform(XTest)

    # Expand basis of the training data and test data
    XTrain = basisExpansion(XTrain, degree)
    XTest = basisExpansion(XTest, degree)

    # Split validation data from training data
    XTrainN, yTrainN, XTrainV, yTrainV = splitData(XTrain, yTrain, validationRatio)

    # Standardize the training data and do the same transformation to the validation data
    standardizeXTrainN = StandardScaler()
    XTrainN = standardizeXTrainN.fit_transform(XTrainN)
    
    # Standardize validation data using training data mean and standard deviation
    XTrainV = standardizeXTrainN.transform(XTrainV)
    
    # Standardize expanded train and test data
    XTrain = standardizeXTrain.fit_transform(XTrain)
    XTest = standardizeXTrain.transform(XTest)

    return XTrain, yTrain, XTrainN, yTrainN, XTrainV, yTrainV, XTest, yTest


## Training/Model Building/Hyper Parameter Selection ##

def chooseHyperParam(XTrainN, yTrainN, XtrainV, yTrainV, isRidge: bool):
    return


if __name__ == "__main__":

    # Read CSV and drop null row in data
    skaterData = pd.read_csv('../data/skater_stats.csv').drop(0)

    # Drop Unnecessary stats
    #skaterData = skaterData.drop(['Rank', 'Skater Shoots', 'Face-off Win Percentage'], axis=1)
    skaterData = skaterData.drop(['Rank'], axis=1)

    #print(skaterData.head())
    #print(skaterData.info())

    y = skaterData['Points Per Game Played']

    #print(y.head())
    #print(y.info())

    X = convertStatsToPG(skaterData.drop('Points Per Game Played', axis=1))

    print(X.head())
    print(X.info())
