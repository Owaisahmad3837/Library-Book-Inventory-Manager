from Configs.json import save_data


def add_data(library_data):

  book_id=input("Enter Book ID :").strip()
  name=input("Enter Book Name :").strip()
  author=input("Enter Book Author :").strip()


  if book_id in library_data:
    return "Aleardy Avabile !"

  library_data[book_id]={
    "name" :name,
    "author":author,
    "issued":False
  }

  print ("Add book Sucessfully...")


  


