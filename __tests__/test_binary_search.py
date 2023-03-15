import random

from algorithms.binary_search import count_guesses_to_find_name


def never_takes_more_than_7_guesses_in_a_list_of_100_ordered_names():
    times_over_seven = 0

    for case in range(10000):
        random_name = names[random.randint(0, 99)]
        guesses_taken = count_guesses_to_find_name(names, random_name)
        if guesses_taken > 7:
            times_over_seven += 1

    assert times_over_seven == 0


names: list[str] = [
    "Aaron Paul",
    "Aidyn Nunez",
    "Aimee Branch",
    "Alaina Skinner",
    "Alani Lee",
    "Alia Harding",
    "Angelo Savage",
    "Armando Howe",
    "Ayla Warner",
    "Azul David",
    "Barrett Berry",
    "Brandon Diaz",
    "Brice Romero",
    "Bryanna Fernandez",
    "Callum Parker",
    "Carlos Ferrell",
    "Carmen Peters",
    "Chasity Monroe",
    "Chloe Giles",
    "Christopher Short",
    "Cindy Molina",
    "Clarence Hall",
    "Clay Scott",
    "Cynthia Gordon",
    "Dana Foley",
    "Dayton Wu",
    "Deven Rivera",
    "Devon Irwin",
    "Eleanor Hudson",
    "Emerson Greene",
    "Emma Stafford",
    "Estrella Cantu",
    "Evelin Crosby",
    "Fatima Ruiz",
    "Felix Knapp",
    "Finn Cherry",
    "Geovanni Melendez",
    "Gilbert Hahn",
    "Grace Bernard",
    "Grace Heath",
    "Grayson Glenn",
    "Hannah Moran",
    "Hannah Ortiz",
    "Harper Freeman",
    "Hayden Cox",
    "Heidi Everett",
    "Holden Bautista",
    "Jaida Atkinson",
    "Jazlyn Bray",
    "Jazlyn Glenn",
    "Jessica Baird",
    "Jett Johns",
    "Justice Wallace",
    "Justin Villarreal",
    "Kasen Webster",
    "Kayley Gilmore",
    "Kaylin Castro",
    "Keira Lutz",
    "Kellen Cherry",
    "Kevin Bentley",
    "Kianna White",
    "Kobe Kirby",
    "Lamar Mullins",
    "Layne Watts",
    "Lewis Hammond",
    "Livia Macdonald",
    "Luciano Morales",
    "Madison Kirby",
    "Maia Palmer",
    "Maia Weeks",
    "Marcel Mayo",
    "Marques Wyatt",
    "Matilda Burch",
    "Matthew Mccullough",
    "Mylie Watts",
    "Nash Jones",
    "Nathan Pham",
    "Niko Graham",
    "Nola Burns",
    "Omar Montes",
    "Oscar Reynolds",
    "Patience Olsen",
    "Payten Wright",
    "Robert Blake",
    "Roderick Morgan",
    "Samir Shaw",
    "Sanaa Haynes",
    "Sanaa Watts",
    "Sarah Bates",
    "Shelby Church",
    "Simon Ashley",
    "Sophia Fernandez",
    "Stephanie Ross",
    "Teagan Roth",
    "Timothy Greene",
    "Turner Drake",
    "Valeria Mccall",
    "Yahir Humphrey",
    "Zain Mcconnell",
    "Zion Freeman",
    "Zwayne Lockwood"
]