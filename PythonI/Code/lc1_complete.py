birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively.

juncos = [i for i in birds if i[0].startswith("Junco ")]
big_birds = [i for i in birds if i[2] >= 19]
latin_names = [i[0] for i in birds]
common_names = [i[1] for i in birds]
body_masses = [i[2] for i in birds]

# (2) Now do the same using conventional loops (you can choose to do this
# before 1 !). 

juncos = []
big_birds = []
latin_names = []
common_names = []
body_masses = []
for i in birds:
    if i[0].startswith("Junco "):
        juncos.append(i)
    if i[2] >+ 19:
        big_birds.append(i)
    latin_names.append(i[0])
    common_names.append(i[1])
    body_masses.append(i[2])

# A nice example out out is:
# Step #1:
# Latin names:
# ['Passerculus sandwichensis', 'Delichon urbica', 'Junco phaeonotus', 'Junco hyemalis', 'Tachycineata bicolor']
# ... etc.
