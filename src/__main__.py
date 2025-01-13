import os
from models import predict_city
import matplotlib.pyplot as plt
if __name__ == "__main__":

    cities = ['Paris','Lyon','Marseille','Lille','Bordeaux','Strasbourg','Rennes','Fort_de_France']

    print('Predict city')
    print('-------------')
    print('Choose a city to predict')
    for i in range(len(cities)):
        print(f'{i+1}. {cities[i]}')
    input_ = int(input('Enter the number of the city: '))-1
    while input_ == 0 or input_ > len(cities):
        'Invalid input. Try again'
        input_ = int(input('Enter the number of the city: '))-1
    city = cities[input_]
    # predictions
    predictions = predict_city(city)
    # store predictions in csv
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, f'../predictions/predictions_{city}.csv')
    predictions.to_csv(filename)
    # plot
    predictions.plot(subplots=True, figsize=(10,10), title=f'Predictions for {city}')
    plt.show()