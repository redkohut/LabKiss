class Computer:
    def __init__(self, brand='Unknown', processor_type='Unknown', processor_freq=1000, ram=2048, disk_mem=256,
                 gpu_spec='Unknown', price=1000):
        self.brand = brand
        self.processor_type = processor_type
        self.processor_freq = processor_freq
        self.ram = ram
        self.disk_mem = disk_mem
        self.gpu_spec = gpu_spec
        self.price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError('brand must be of type str')
        self.__brand = value

    @property
    def processor_type(self):
        return self.__processor_type

    @processor_type.setter
    def processor_type(self, value):
        if not isinstance(value, str):
            raise TypeError('processor type must be of type str')
        self.__processor_type = value

    @property
    def processor_freq(self):
        return self.__processor_freq

    @processor_freq.setter
    def processor_freq(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('processor frequency must be of type float or int')
        if value <= 0:
            raise ValueError('processor frequency in GHz must be greater than 0')
        self.__processor_freq = value

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, value):
        if not isinstance(value, int):
            raise TypeError('ram must be of type int')
        if value <= 0:
            raise ValueError('ram in MB must be greater than 0')
        self.__ram = value

    @property
    def disk_mem(self):
        return self.__disk_mem

    @disk_mem.setter
    def disk_mem(self, value):
        if not isinstance(value, int):
            raise TypeError('disk memory must be of type int')
        if value <= 0:
            raise ValueError('disk memory in GB must be greater than 0')
        self.__disk_mem = value

    @property
    def gpu_spec(self):
        return self.__gpu_spec

    @gpu_spec.setter
    def gpu_spec(self, value):
        if not isinstance(value, str):
            raise TypeError('gpu spec must be of type str')
        self.__gpu_spec = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError('price must be of type int')
        if value < 0:
            raise ValueError('price must not be less than 0')
        self.__price = value

    def __eq__(self, other):
        if isinstance(other, Computer):
            return self.brand == other.brand
        return False

    def __hash__(self):
        return hash(self.brand)

    def __str__(self):
        return f'Computer: brand={self.brand}, processor_type={self.processor_type}, ' \
               f'processor_freq={self.processor_freq}, ram={self.ram}, disk_mem={self.disk_mem},' \
               f' gpu_spec={self.gpu_spec}, price={self.price}'


class PriceList:
    def __init__(self, firm, *argc):
        self.firm = firm
        self.computers = argc

    @property
    def firm(self):
        return self.__firm

    @firm.setter
    def firm(self, value):
        if not isinstance(value, str):
            raise TypeError('firm must be of type str')
        self.__firm = value

    @property
    def computers(self):
        return self.__computers

    @computers.setter
    def computers(self, computers):
        if any(not isinstance(computer, Computer) for computer in computers):
            raise TypeError("computers must be of Computer type")
        self.__computers = list()
        for computer in computers:
            self.add_computer(computer)

    def add_computer(self, computer):
        if not isinstance(computer, Computer):
            raise TypeError('computer must be of type Computer')
        if computer in self.__computers:
            raise ValueError('there are already such computer brand in a price list')
        self.__computers.append(computer)

    def update_computer(self, brand, new_computer):
        if not isinstance(brand, str):
            raise TypeError('brand must be of type str')
        if not any(computer.brand == brand for computer in self.computers):
            raise ValueError('there are no such computer brand in the price list')
        for i, computer in enumerate(self.computers):
            if computer.brand == brand:
                self.computers[i] = new_computer
                break

    def delete_computer(self, brand):
        if not isinstance(brand, str):
            raise TypeError('brand must be of type str')
        temp_computer = Computer(brand)
        self.computers.remove(temp_computer)

    def search_brand(self, processor_type, processor_freq, ram, disk_mem, gpu_spec, price):
        # just to validate arguments
        searched_computer = Computer('', processor_type, processor_freq, ram, disk_mem, gpu_spec, price)

        for computer in self.computers:
            if (computer.processor_type, computer.processor_freq, computer.ram, computer.disk_mem, computer.gpu_spec,
                computer.price) \
                    == (processor_type, processor_freq, ram, disk_mem, gpu_spec, price):
                return computer.brand

    def __str__(self):
        computers = '\n\t'.join(map(str, self.computers))
        return f'Price list for firm={self.firm}:\n\t{computers}'


def main():
    try:
        comp1 = Computer('first')
        comp2 = Computer('second')
        price_list = PriceList('my_firm', comp1, comp2)
        print(price_list)
        comp3 = Computer('first', 'new_value')
        price_list.update_computer('first', comp3)
        print(price_list)
        comp4 = Computer('fourth')
        price_list.add_computer(comp4)
        print(price_list)
        price_list.delete_computer('second')
        print(price_list)

    except Exception as e:
        print(e)


main()
