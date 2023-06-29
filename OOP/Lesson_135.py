class SuperList(list):
    def __len__(self):
        return 5


my_super = SuperList([1,2,3,4]);
print(dir(my_super))
print(f'List length {len(my_super)} \n Items: {my_super}')
my_super.append(5)
print(f'List length {len(my_super)} \n Items: {my_super}')
print(issubclass(SuperList, list))