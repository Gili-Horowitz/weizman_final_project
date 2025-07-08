
from DataBase import add_to_cart as db_add_to_cart

ideams = {"ברבי":55,
          "בובת דובי":35,
          "מכונית":20,
          "לגו":60,
          "כדור":15,
          "טאקי":40,
          "פליימוביל":75,
          "חוברת צביעה":15,
          "מנורה":30,
          "דינוזאורים":35,
          "בובת חתול":50,
          "מטוס":25
          }

cart_ideams={}




def add_to_cart(ideam_name):
   print(cart_ideams)
   cart_ideams[ideam_name]=ideams.get(ideam_name)
   print(cart_ideams)
   if customer_id is not None and product_id is not None:
       db_add_to_cart(customer_id, product_id)


   #print(cart_ideams)
#add_to_cart(ideam_name)
#print(cart_ideams)