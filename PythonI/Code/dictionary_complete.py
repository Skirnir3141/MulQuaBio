taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a python script to populate a dictionary called taxa_dic derived from
# taxa so that it maps order names to sets of taxa and prints it to screen.
# 
# An example output is:
#  
# 'Chiroptera' : set(['Myotis lucifugus']) ... etc. 
# OR, 
# 'Chiroptera': {'Myotis  lucifugus'} ... etc

# Capture distinct orders
orders = []
for i in taxa:
    if i[1] not in orders:
        orders.append(i[1])

# Create dic and populate order names for keys and empty lists for values
taxa_dic = {}
for i in orders:
    taxa_dic[i] = []

# Populate empty list with species
for i in taxa:
    taxa_dic[i[1]].append(i[0])


# Now write a list comprehension that does the same (including the printing after the dictionary has been created)  

# Took the basic solution from stackoverflow...more or less understand what it's doing...seems 
# like an example of a too complicated comprehension and this would be much more readable if done with loops.
print({val: [key for key, vv in dict(taxa).items() if vv == val] for val in dict(taxa).values()})

