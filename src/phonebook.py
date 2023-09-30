class Phonebook:
    #construtor python 
    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nme invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalio'
        if '%' in name:
            return 'Nome invalido'

        if len(number) < 0:
            return 'Numero invalid'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome invaldo'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nme invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome nvalido'

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self): # 
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            # if search_name in name: deveria ser in name no lugar de not in
            if search_name not in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """ 
        # retorna somente o dicionario como foi incluido 
        # >>> # Sort by key
        # >>> dict(sorted(people.items()))
        # {1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}
        return self.entries

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        # retorna somente o dicionario como foi incluido 
        # >>> # Sort by key
        # >>> dict(sorted(people.items()))
        # {1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}

        return self.entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'


# idiomas sendo usados incorretamente linha 25 "Numero invalid"

pb = Phonebook()
#print(pb.entries)
pb.clear()
pb.add(name='huginho', number='123')
pb.add(name='zezinho', number='456')
pb.add(name='luizinho', number='789')
#print(pb.lookup('huginho')) # retorna o numero do caboclo.
#print(pb.get_names()) #retorna os nomes dos caras da agenda
#print(pb.search('zinho'))
#print(pb.get_phonebook_sorted())

pb.delete('zezinho')
pb.delete('luizinho')
pb.delete('huginho')
pb.delete('huginho')
print(pb.entries)