from borrow import borrow

borrow1 = borrow("sama", 503, "zekala", 855)
borrow2 = borrow("semo", 500, "arses", 10445)

print(borrow1.name , borrow1.membership_id)
print(borrow1.borrow_book())
print(borrow2.borrow_book())

