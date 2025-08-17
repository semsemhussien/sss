class borrow:
    def __init__(self, name, membership_id, title, isbn):
        self.name = name
        self.membership_id = membership_id
        self.title = title
        self.isbn = isbn

    def borrow_book(self):
        if self.isbn >= 9876:
            return True
        else:
            return False    

        
    

    
    