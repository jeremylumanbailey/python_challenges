filepath = './input.txt'
backup_images = [] # projects.doc
file_names = [] # customers.dat_1539026253_FULL
space_found = False

orphan_files = [] # F customers.dat_1539026253_FULL
index_orphans = [] # I products.txt

with open(filepath, "r") as fp:
    for line in fp:
        if line in ['\n', '\r\n']:
            space_found = True
            continue
        if not space_found:
            backup_images.append(line.strip())
        else:
            file_names.append(line.strip())

print(backup_images)
print()
print(file_names)
print()
def image_exist(y):
    for x in range(0, len(file_names)):
        if backup_images[y] in file_names[x]:
            return True
    return False


for i in range(0, len(backup_images)):
   if not image_exist(i):
       index_orphans.append("I " + backup_images[i])





for i in range(0, len(file_names)):
    continue


print(index_orphans)

