Books_list = ["The Great Gatsby", "Ulysses", "In Search of Lost Time", "One Hundred Years of Solitude", "The Catcher in the Rye"]
Author_list = ["F. Scott Fitzgerald", "James Joyce", "Marcel Proust", "Gabriel García Márquez", "J. D. Salinger"]
Books_genre_list = ["Tragedy", "Modernist novel", "Philosophical fiction", "Novel", "Realistic fiction"]
Books_date_list = [1925, 1920, 1913, 1967, 1951]
Books_ratings_list = [3.9, 3.8, 4.3, 4.1, 3.8]

print("Books Data:")
for i in range(len(Books_list)):
    print(f"Ratings: {Books_ratings_list[i]}, Title: {Books_list[i]}, Author: {Author_list[i]}, Genres: {Books_genre_list[i]}, Publish Year: {Books_date_list[i]}")
