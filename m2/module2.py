# CSC500 Module 2 Assignment
# Lists in Real-Life Applications

# The first three books in Glenda's book database
books = [
    {
        "isbn": "9780618002214",
        "title": "The Hobbit, Or, There And Back Again",
        "authors": ["John Ronald Reuel Tolkien"],
        "publisher": "Houghton Mifflin Harcourt",
        "publication_year": 1997,
        "language": "en"
    },
    {
        "isbn": "9780373895915",
        "title": "How Nancy Drew Saved My Life",
        "authors": ["Lauren Baratz-Logsted"],
        "publisher": "",
        "publication_year": 2006,
        "language": "en"
    },
    {
        "isbn": "9781101875612",
        "title": "The Hopefuls",
        "authors": ["Jennifer Close"],
        "publisher": "Knopf",
        "publication_year": 2016,
        "language": "en"
    }
]

# Display each book's title and author
for book in books:
    print(book["title"], "-", book["authors"][0])
