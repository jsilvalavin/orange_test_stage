# imports
from data_processing import data_processing
from feature_engineering import feature_engineering
from statsmodels.api import OLS, add_constant
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

#### parameters ####
future_index = pd.date_range(start="2025-01-01",end="2025-03-31")

# data
data = data_processing()
data = feature_engineering(data)

# normalize to stationarity
def normalize(X,y):
    x = X['ordinal']
    x_with_int = add_constant(x)
    model = OLS(y,x_with_int).fit()
    y_pred = model.predict(x_with_int)
    return y - y_pred, model

# predict variables
def predict_vars(X, future_index):
    # columns for predicting
    cols = ['marketing_score', 'competition_index', 'customer_satisfaction', 'purchasing_power_index', 'weather_condition', 'tech_event','store_traffic','public_transport']
    time_cols = time_cols = ['day_of_week', 'month','quarter', 'year', 'day_of_year', 'ordinal']
    # dataframe
    X_pred = pd.DataFrame(index=future_index, columns=X.columns)
    X_pred = feature_engineering(X_pred)
    # for variable
    for col in cols:
        y = X[col]
        y, model = normalize(X,y)
        # model fit
        reg = xgb.XGBRegressor(n_estimators=1000, learning_rate=0.01)
        reg.fit(X[time_cols], y, verbose=False)
        # predict
        y_pred = reg.predict(X_pred[time_cols])
        # denormalize
        y_pred = y_pred + model.predict(add_constant(X_pred['ordinal']))
        # add to dataframe
        X_pred[col] = y_pred
    # for 5g_phase
    ordinals = pd.concat([X['ordinal'],X_pred['ordinal']],axis=0)
    ordinals = ordinals.values.reshape(-1,1)
    #
    ordinals = StandardScaler().fit_transform(ordinals)
    model = LogisticRegression(multi_class='multinomial', solver = 'lbfgs', max_iter=500)
    model.fit(ordinals[:len(X)],X['5g_phase'])
    #
    y_pred = model.predict(ordinals[len(X):])
    X_pred['5g_phase'] = y_pred
    
    return X_pred

# normalize data
def normalize_data(X,X_pred):
    # columns to normalize
    cols = ['marketing_score', 'competition_index', 'customer_satisfaction', 'purchasing_power_index', 'weather_condition', 'tech_event','store_traffic','public_transport']
    # all data
    X_total = pd.concat([X,X_pred],axis=0)
    X_total_normalized = X_total.copy()
    models = {}
    # for variable
    for col in cols:
        y = X_total[col]
        y, model = normalize(X_total,y)
        models[col] = model
        X_total_normalized[col] = y
    # separate data again
    X_normalized = X_total_normalized.iloc[:len(X)]
    X_pred_normalized = X_total_normalized.iloc[len(X):]
    # return 
    return X_normalized, X_pred_normalized, models     

# predict
def predict(X_normalized, y_normalized, X_pred_normalized):
    reg = xgb.XGBRegressor(n_estimators=1000, learning_rate=0.01)
    reg.fit(X_normalized, y_normalized, verbose=False)
    y_pred = reg.predict(X_pred_normalized)
    return y_pred

# predict city
def predict_city(city):
    # city data
    df_city = data[data['city'] == city]
    df_city = df_city.drop(columns=['city'])
    df_city = df_city.dropna()
    # phones
    phones = ['jPhone_Pro_revenue','Kaggle_Pixel_5_revenue','Planet_SX_revenue']
    # predictors
    X = df_city.drop(columns=phones)
    # predict each phone
    predictions = pd.DataFrame(index=future_index, columns=phones)
    for phone in phones:
        # target var
        y = df_city[phone]
        # pred vars
        X_pred = predict_vars(X, future_index)
        # normalize
        X_normalized, X_pred_normalized, models = normalize_data(X,X_pred)
        y_normalized, model = normalize(X,y)
        # predict
        y_pred = predict(X_normalized, y_normalized, X_pred_normalized)
        # denormalize
        y_pred = y_pred + model.predict(add_constant(X_pred['ordinal']))
        # add to dict
        predictions[phone] = y_pred
        # print
        print(phone)
    # return
    return predictions