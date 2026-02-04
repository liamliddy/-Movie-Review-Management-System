#PROJECT 3 LIAM LIDDY
#Write movie records 
def write_records():
    print("\nWrite Records:\n")
    while True:
        try:
            movies = int(input("How many movies would you like to enter?: "))
            with open("movie_records.txt","a") as f:
                for i in range(movies):
                    movie = input("What is the title of the movie?: ").strip().title()
                    genre = input("What is the genre?: ").strip().title()
                    year =input("What year was it released?: ")
                    f.write(f"{movie}\n{genre}\n{year}\n")
                break  
        except ValueError:
            print("Please enter a number.")

#Ask the user to write reviews for records 
def write_review_csv():
    import csv
    print("\nWrite Reviews:\n")
    while True:
        with open("movie_records.txt","r") as f:
            m = f.readlines()
            movies = [m[i].strip()for i in range(0,len(m),3)]
            while True:
                movie = input("What is the title of the movie?: ").strip().title()
                if movie in movies:
                    break
                else:
                    print("Movie is not in records, please try another.")

        review = input("Write your review: ")
        while True:
            rating = input("Rate(1-10): ")
            if rating.isdigit() and 1 <= int(rating) <= 10:
                break
            else:
                print("Please enter a number between 1-10")

        
        with open("movie_review.csv", "a", newline = '') as f:
            writer = csv.writer(f)
            writer.writerow([movie,review, rating])
        while True:
            again = input("Would you like to write another review (yes/no)?: ").strip().lower()
            if again == "no":
                break
            elif again == "yes":
                break
            else:
                print("Please enter 'yes' or 'no'.")
        if again == "no":
            break
                

#Display each movie records to the user
def display_movies():
    print("\nMovie Records:\n")
    with open("movie_records.txt","r") as f:
        while True:
            movie = f.readline().rstrip()
            if not movie:
                break
            genre = f.readline().rstrip()
            year = f.readline().rstrip()
            print(f"Movie : {movie} / Year : {year} / Genre : {genre}")
            
#Display reviews/averages to the user
def display_reviews():
    import csv
    print("\nMovie Reviews:\n")
    movies = {}
    ratings = {}
    with open("movie_review.csv", "r") as f:
        reader = csv.reader(f)
        for review in reader:
            print('Reviews:', review)

            movie = review[0]
            rating = float(review[2])
            if movie in ratings:
                ratings[movie] += rating
                movies[movie] += 1
            else:
                ratings[movie] = rating
                movies[movie] = 1

    for movie in ratings:
        average = ratings[movie] / movies[movie]
        print(f"{movie} / Average Rating: {average:.2f}")

#Allow the user to search through records 
def movie_search():
    print("\nMovie Catalog Search:\n")
    while True:
        search = input("What movie would you like to search for?: ") .strip().title()
        found = False
        with open("movie_records.txt","r") as f:
            while True:
                movie = f.readline().rstrip()
                if not movie:
                    break
                genre = f.readline().rstrip()
                year = f.readline().rstrip()
                
                if movie.strip() == search:
                    print("Movie is in records!")
                    print(f"Movie : {movie} / Year : {year} / Genre : {genre}")
                    found = True
                    break
        if not found:
            print("Movie is not in records, try again.")

                
        while True:
            again = input("Would you like to search for another movie (yes/no)?: ").strip().lower()
            if again == "no":
                return
            elif again == "yes":
                break
            else:
                print("Please enter 'yes' or 'no'.")
                continue
                       

                    
#Ask user if they would like to modify one of the records
def modify_record():
    import os
    print("\nMovie Genre Modification:\n")

    found = False
    with open("movie_records.txt","r") as f:
        m = f.readlines()
    movies = [m[i].strip()for i in range(0,len(m),3)]

    while True:
        search = input("What record would you like to modify?: ").strip().title()
        if search in movies:
            break
        else:
            print("Movie is not in records, please try another.")
    new_genre = input("Enter the new genre: ").strip().title()
    
    with open("movie_records.txt","r") as f, open("temp_movie_records.txt","w") as tf:
        movie = f.readline()
        while movie != "":
            genre = f.readline().rstrip()
            year = f.readline().rstrip()
            if movie.strip() == search:
                tf.write(f"{movie}")
                tf.write(f"{new_genre}\n")
                tf.write(f"{year}\n")
                found = True
            else:
                tf.write(f"{movie}")
                tf.write(f"{genre}\n")
                tf.write(f"{year}\n")
            movie = f.readline()
    os.remove("movie_records.txt")
    os.replace("temp_movie_records.txt","movie_records.txt")

    if found:
        print("The file has been updated.")
    else:
        print("The item was not found.")
    
#Ask user what record they would like to delete
def delete_record():
    import os
    print("\nMovie Deletion:\n")
    found = False

    with open("movie_records.txt","r") as f:
        m = f.readlines()
    movies = [m[i].strip()for i in range(0,len(m),3)]
    while True:
        search = input("What record would you like to delete?: ").strip().title()
        if search in movies:
            break
        else:
            print("Movie is not in records, please try another.")

    
    with open("movie_records.txt","r") as f, open("temp_movie_records.txt","w") as tf:
        movie = f.readline()
        while movie != "":
            genre = f.readline().rstrip()
            year = f.readline().rstrip()
            if movie.strip() == search:
                found = True
            else:
                tf.write(f"{movie}")
                tf.write(f"{genre}\n")
                tf.write(f"{year}\n")
            movie = f.readline()
    os.remove("movie_records.txt")
    os.replace("temp_movie_records.txt","movie_records.txt")

    if found:
        print(f"{search} has been deleted.")
    else:
        print("The item was not found.")
    
#Once user has created database, they can chose between a list of menu options
def configured_database():
    while True:
        print("\nMovie Review Management System:")
        print("1. Write Records: ")
        print("2. Write Reviews: ")
        print("3. Display Movies: ")
        print("4. Display Reviews: ")
        print("5. Movie Search: ")
        print("6. Modify Records: ")
        print("7. Delete Records: ")

        menu = input("Hello, what would you like to select? :")
        if menu == '1':
            write_records()
        elif menu == '2':
            write_review_csv()
        elif menu == '3':
            display_movies()
        elif menu == '4':
            display_reviews()
        elif menu == '5':
            movie_search()
        elif menu == '6':
            modify_record()
        elif menu == '7':
            delete_record()
        else:
            print("Please enter a number between 1-7")


def main():
##  write_review_manual()
##  def write_review_manual():  
##      movie = input("What is the title of the movie? ")
##      review = input("Write your review: ")
##      rating =input("Rate(1-10): ")
##      with open("movie_review.csv", "a") as f:
##          f.write(f"{movie},{review},{rating}\n")
    
    write_records()
    write_review_csv()
    display_movies()
    display_reviews()
    movie_search()
    modify_record()
    delete_record()
    configured_database()
main()
    
                       
                       
        
