from sqlalchemy.orm import sessionmaker
from modules.darbuotojas import engine, Darbuotojas
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

def atvaizduoti_visus():
    darbuotojai = session.query(Darbuotojas).all()
    print("------------Darbuotojai-------------")
    for darbuotojas in darbuotojai:
        print(darbuotojas)
    print("----------------------------------")

while True:
    choice = int(input("1 - atvaizduoti \n2 - įvesti \n3 - redaguoti \n4 - ištrinti \n0 - išeiti"))
    match choice:
        case 1:
            atvaizduoti_visus()
        case 2:
            pass
            vardas = input("Vardas: ")
            pavarde = input("Pavardė: ")
            gimimo_data = datetime.strptime(input("Gimimo data (YYYY-MM-DD): "), "%Y-%m-%d")
            atlyginimas = float(input("Atlyginimas: "))
            darbuotojas = Darbuotojas(vardas, pavarde, gimimo_data, atlyginimas)
            session.add(darbuotojas)
            session.commit()
        case 3:
            atvaizduoti_visus()
            red_id = int(input("Įveskite redaguojamo ID: "))
            red_irasas = session.query(Darbuotojas).get(red_id)
            red_irasas.vardas = input("Vardas: ")
            red_irasas.pavarde = input("Pavardė: ")
            red_irasas.gimimo_data = datetime.strptime(input("Gimimo data (YYYY-MM-DD): "), "%Y-%m-%d")
            red_irasas.atlyginimas = float(input("Atlyginimas: "))
            session.commit()
        case 4:
            atvaizduoti_visus()
            trin_id = int(input("Įveskite trinamo ID: "))
            trin_irasas = session.query(Darbuotojas).get(trin_id)
            session.delete(trin_irasas)
            session.commit()
        case 0:
            print("Viso gero")
            break
