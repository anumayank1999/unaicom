def prediction_model(pclass,sex,age,sibs,parch,fare,embarked,title):
    import pickle
    x=[[pclass,sex,age,sibs,parch,fare,embarked,title]]
    randomForest = pickle.load(open('E:/fullstck/Django+ML+AWS/titanic/titanic/titanic_model.sav','rb'))
    predictions=randomForest.predict(x)
    return predictions