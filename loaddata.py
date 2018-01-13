from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database
from models import Category, Item, User, Base

engine = create_engine('sqlite:///catalog.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create a user
user = User(name="Moses Maxwell", email="mosesmaxwell@gmail.com",
             photo='https://media-exp2.licdn.com/mpr/mpr/shrinknp_400_400/AAIAAwDGAAAAAQAAAAAAAAw1AAAAJGJhOTM0ZTkzLWMwNTctNDkyYS04YTNmLTlmMjVjNjhhYThlZg.jpg')
session.add(user)
session.commit()

# Soups
category1 = Category(name="Soup", user_id=1)

session.add(category1)
session.commit()

item1 = Item(name="Long Soup", user_id=1, description="Egg drop soup is a Chinese soup of wispy beaten eggs in boiled chicken broth. Condiments such as black pepper or white pepper, and finely chopped scallions and tofu are optional, but commonly added to the soup.", category=category1)
session.add(item1)
session.commit()

item2 = Item(name="Short Soup", user_id=1,  description="Short soup and its companion long soup are indeed Australian terms for Chinese wonton soup and Chinese noodle soup respectively. The name long soup probably derives from an English speaker's way of describing the kind of noodle typically found in the dish; long soup contains long, thin noodles.", category=category1)
session.add(item2)
session.commit()

item3 = Item(name="Sweet Corn Soup", user_id=1, description="Corn soup is a soup made of corn. It was normally made in corn producing areas of the world, but is now widespread because of greater corn distribution.", category=category1)
session.add(item3)
session.commit()

item4 = Item(name="Chicken Clear soup Soup", user_id=1, description="Chicken soup is a soup made from chicken, simmered in water, usually with various other ingredients. The classic chicken soup consists of a clear chicken broth, often with pieces of chicken or vegetables; common additions are pasta, dumplings, or grains such as rice and barley.", category=category1)
session.add(item4)
session.commit()

# Starter
category2 = Category(name="Starter", user_id=1)

session.add(category2)
session.commit()

item1 = Item(name="Chicken 65", user_id=1, description="Chicken 65 is a spicy, deep fried chicken dish originating from Chennai, India, as an entree, or quick snack. The flavour of the dish can be attributed to red chillies but the exact set of ingredients for the recipe can vary. It can be prepared using boneless or bone in chicken and is usually served with onion and lemon garnish.", category=category2)
session.add(item1)
session.commit()

item2 = Item(name="Fish Finger", user_id=1,  description="Fish fingers (British English) or fish sticks (American English), are a processed food made using a whitefish, such as cod, hake, haddock or pollock, which has been battered or breaded.", category=category2)
session.add(item2)
session.commit()

item3 = Item(name="Mutton Kebab", user_id=1, description="Kebab dishes can consist of cut up or ground meat or seafood, sometimes with fruits and vegetables; cooked on a skewer over a fire, or like a hamburger on a grill, baked in a pan in an oven, or as a stew; and served with various accompaniments according to each recipe.", category=category2)
session.add(item3)
session.commit()

# Biriyani
category3 = Category(name="Biriyani", user_id=1)

session.add(category3)
session.commit()

item1 = Item(name="Chicken Biriyani", user_id=1, description="Chicken Biryani also known as biriyani, biriani, birani or briyani, is a South Asian mixed rice dish with its origins among the Muslims of the Indian subcontinent. It is popular throughout the Indian subcontinent and among the diaspora from the region.", category=category3)
session.add(item1)
session.commit()

item2 = Item(name="Mutton Biriyani", user_id=1,  description="Mutton Biryani also known as biriyani, biriani, birani or briyani, is a South Asian mixed rice dish with its origins among the Muslims of the Indian subcontinent. It is popular throughout the Indian subcontinent and among the diaspora from the region.", category=category3)
session.add(item2)
session.commit()

item3 = Item(name="Prawn Biriyani", user_id=1, description="Prawn Biryani also known as biriyani, biriani, birani or briyani, is a South Asian mixed rice dish with its origins among the Muslims of the Indian subcontinent. It is popular throughout the Indian subcontinent and among the diaspora from the region.", category=category3)
session.add(item3)
session.commit()

item4 = Item(name="Fish Biriyani", user_id=1, description="Fish Biryani also known as biriyani, biriani, birani or briyani, is a South Asian mixed rice dish with its origins among the Muslims of the Indian subcontinent. It is popular throughout the Indian subcontinent and among the diaspora from the region.", category=category3)
session.add(item4)
session.commit()

# Rice
category4 = Category(name="Rice", user_id=1)

session.add(category4)
session.commit()

item1 = Item(name="Fried Rice", user_id=1, description="Fried rice is a dish of cooked rice that has been stir fried in a wok or a frying pan and is usually mixed with other ingredients such as eggs, vegetables, seafood, or meat. It is often eaten by itself or as an accompaniment to another dish.", category=category4)
session.add(item1)
session.commit()

item2 = Item(name="Plain Rice", user_id=1,  description="Plain Rice medium grain rice is used extensively in Japan, including to accompany savoury dishes, where it is usually served plain in a separate dish.", category=category4)
session.add(item2)
session.commit()

item3 = Item(name="Gee Rice", user_id=1, description="Gee Rice medium grain rice is used extensively in Japan, including to accompany savoury dishes, where it is usually served plain in a separate dish.", category=category4)
session.add(item3)
session.commit()

item4 = Item(name="Curd Rice", user_id=1, description="Curd Rice medium grain rice is used extensively in Japan, including to accompany savoury dishes, where it is usually served plain in a separate dish.", category=category4)
session.add(item4)
session.commit()

# Drinks
category5 = Category(name="Drinks", user_id=1)

session.add(category5)
session.commit()

item1 = Item(name="Lemon Juice", user_id=1, description="Lemon Juice is a beverage made from the extraction or pressing out of the natural liquid contained in fruit and vegetables.", category=category5)
session.add(item1)
session.commit()

item2 = Item(name="Apple Juice", user_id=1,  description="Apple Juice is a beverage made from the extraction or pressing out of the natural liquid contained in fruit and vegetables.", category=category5)
session.add(item2)
session.commit()

item3 = Item(name="Orange Juice", user_id=1, description="Orange Juice is a beverage made from the extraction or pressing out of the natural liquid contained in fruit and vegetables.", category=category5)
session.add(item3)
session.commit()

item4 = Item(name="Milk Shake", user_id=1, description="Milk Shake is a beverage made from the extraction or pressing out of the natural liquid contained in fruit and vegetables.", category=category5)
session.add(item4)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
