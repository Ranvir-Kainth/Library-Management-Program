#open book data file to obtain library of books
#import json to obtain book data contained in a
#separate json file
import json

#open and read json file containing book data to retrieve list of books
#with info of each book in the list(title, author, publication year, genre, price) 
#stored in a dictionary
with open("books.json", "r") as json_file:
    #load data and assign to variable "library"
    library = json.load(json_file)

#Create a funciton for adding new books to library
def add_book():
    print()
    title = input("Please enter the title: ")
    author = input("Please enter the author: ")
    genre = input("Please enter the genre: ")
    try:
        year = int(input("Please enter the publication year e.g. 1992: "))
    except ValueError as e:
        print("Error", e)
        #Handle error gracefully
        print("Invalid value. Please enter year in numbers(integer).")
    try:
        price = float(input("Please enter the price : "))
    except ValueError as e:
        print("Error", e)
        print("Invalid value. Please enter a price in numbers(integer), in pounds and pence.")
        return add_book()
    #Set variable "new book" to contain the details of the new book in a dictionary
    #in the same format as the other books in the library.
    new_book = {
                "title":title, 
                "author": author, 
                "genre": genre,
                "publication year": year,  
                "price": price
                }
    #add the new book to the library
    library.append(new_book)
    print()
    print(library)
    print()
    print("Book added to the collection.")
    return library

#Create functin to search for book by title
def search_title():
    #Ask user to enter titles 
    title = input("Please enter the title: ")
    #iterate through items and index
    for index, items in enumerate(library, start =1):
    #if items with key, "title" has a value equal to to enterted title
        if items["title"] == title:
            print("Book availabe: ", index, items) 
    print("\nIf not shown, the title is not in the library.")
    
#Create function to sort books alphabetically by title.
def sort_alphabetically():
    #create new list to contain sorted titles by 
    #applying sorted() function to library, and sort title  
    #speficifcally using lambda to customize the sort order of the key, "title"
    sorted_list = sorted(library, key=lambda d: d["title"])
    #get list of sort titles only 
    #iterate through sorted_list
    for i in sorted_list:
        sorted_title_list = (i.get("title"))
        print()
        print(sorted_title_list)

#Create function for finding oldest book in library
def oldest_book():
    #sort library list by year, from oldest to newest
    sorted_list = sorted(library, key = lambda d: d["publication year"])
    #print oldest year which will be the first item in the list

    print("\nOldest book: \n", sorted_list[0])

#Create function for finding newest book in library
def newest_book():
    #sort library list by year, from newest to oldest
    #reverse the sorted list to get decsending order 
    sorted_list = sorted(library, key = lambda d: d["publication year"], reverse = True)
    #print newest year which will be the first item in the list
    print()
    print("Newest Book: \n", sorted_list[0])

#Create function to export a list titles to a CSV file
def export_titles():
    #Create a blank list to hold titles
    title_list = []
    #for items in the library list
    for i in library:
        #Get the titles from each item and assign to titles
        titles = (i.get("title"))
        #add titles to titles_list to create a list
        title_list.append(titles)
    
    #import csv in order to write to a csv file
    import csv
    #open the csv file to write
    with open('titles.csv', 'w', newline = '') as file:
        #create writer to wrtie in csv format
        writer = csv.writer(file)
        #write the info in list of book titles
        writer.writerow(title_list)
        print("\n Titles exported successfully to CSV file.")

#Create function to export array of years to csv file
def export_years():
    #import array function to use array
    import array
    #create empty array of integers
    years_array = array.array('i',[])
    
    for i in library:
        #Get the publication years from each item and assign to years
        years = (i.get("publication year"))
        #add titles to titles_list to create a list
        years_array.append(years)
    
    #import csv in order to write to a csv file
    import csv
    #open the csv file to write
    with open('years.csv', 'w', newline = '') as file:
        #create writer to wrtie in csv format
        writer = csv.writer(file)
        #write the info in list of book titles
        writer.writerow(years_array)
        print("\n Publication years exported successfully to CSV file.")

#Create function to count books by a specific author
def count_titles():
    #Creat blank list to hold authors
    authors_list = []
    #iterate through library and retrieve authors 
    for i in library:
        author_values = i.get("author")
    #add authors to authors list
    authors_list.append(author_values)
    #ask user to enter author
    author_input = input("\nPlease enter the author: ")
    #set count to zero as a starting poit
    count = 0
    for author in authors_list:
        if author == author_input:
            count +=1
    print(f"\nThere is/are {count} title(s) available by {author_input}.")

#Function to apply to main body of code containing menu and acting on choice
def main():

    while True: 
        print()
        print("Book Management Application")
        print()
        print("1. Add New Book")
        print("2. Search for book by title")
        print("3. Sort books alphabetically by title")
        print("4. Find oldest book in collection")
        print("5. Find newest book in collection")
        print("6. Export book titles to CSV file")
        print("7. Export years of books CSV file")
        print("8. Count number of titles based on author")
        print("9. Exit Program")
        print()
        try:
            choice = int(input("Select an option from the menu below by typing in the number (1 - 9): "))
        except ValueError as e:
            print("\nError", e)
            print("Invalid value. Please enter an integer (number) from 1 - 9")
        
        if choice == 1:
            add_book()
        elif choice == 2:
            search_title()
        elif choice == 3:
            sort_alphabetically()
        elif choice == 4: 
            oldest_book()
        elif choice == 5:
            newest_book()
        elif choice == 6:
            export_titles()
        elif choice == 7:
            export_years()
        elif choice == 8:
            count_titles()    
        elif choice == 9:
            print("\nYou have now exited the program. Goodbye.")
            break
        else:
            print("\nInvalid value. Please enter an integer (number) from 1 - 9")

#Main body 
main() 





