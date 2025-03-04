from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Company, Dev, Freebie, Base

# Connect to the database
engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()

# Drop existing tables and recreate them (only for resetting data)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create Companies
company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Facebook", founding_year=2004)
company3 = Company(name="Microsoft", founding_year=1975)

# Create Developers
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
dev3 = Dev(name="Charlie")

# Create Freebies
freebie1 = Freebie(item_name="T-shirt", value=10, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Sticker", value=2, company=company2, dev=dev2)
freebie3 = Freebie(item_name="Mug", value=5, company=company1, dev=dev3)
freebie4 = Freebie(item_name="Backpack", value=25, company=company3, dev=dev1)
freebie5 = Freebie(item_name="Notebook", value=8, company=company2, dev=dev3)

# Add all instances to the session
session.add_all([company1, company2, company3, dev1, dev2, dev3, freebie1, freebie2, freebie3, freebie4, freebie5])

# Commit the session to save changes
session.commit()

print("Database seeded successfully!")
