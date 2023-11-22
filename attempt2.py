import csv

def highest_grossing_film(list_of_movies):
    highest_film_money = 0
    highest_film_name = None

    for dict in movie_list:
        movie_title = dict['Title']
        domestic_sales = int(dict['Domestic Sales'])
        if highest_film_money < domestic_sales:
            highest_film_money = domestic_sales
            highest_film_name = movie_title

    return highest_film_money, highest_film_name


with open('movie_data_shuffled.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    movie_list = []

    for row in csv_reader:
        movie_dict = {
            'Title': row[0],
            'Year': row[1],
            'Distributor': row[2],
            'Budget': row[3],
            'Domestic Opening': row[4],
            'Domestic Sales': row[5],
            'International Sales': row[6],
            'World Wide Sales': row[7],
            'Release Date': row[8],
            'Running Time': row[9],
            'License': row[10]
        }

        movie_list.append(movie_dict)

x = highest_grossing_film(movie_list)
print(x)


