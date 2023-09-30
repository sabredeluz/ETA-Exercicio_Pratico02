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
            return 'Nome invalido'  #1  alterando de Nme invalido' para 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'   #2  alterando de Nome invalio' para 'Nome invalido'
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
            return 'Nome invalido'   #3 alterando de Nme invaldo' para 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'    #4 alterando de Nme invaldo' para 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'     #5  alterando de Nome nvaldo' para 'Nome invalido'

        name_found = False
        for local_name in self.entries.keys():
            if local_name == name:
                return self.entries[name]
        if not name_found:
            return 'Name not found' #6 implementada mensagem caso o nome nao esteja no dicionario






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
            if search_name in name:  # 7 - removemos o not dessa linha
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
        #print(list(self.entries.keys()))
        #print(list(sorted(self.entries.keys())))
        return sorted(self.entries.keys())

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        # retorna somente o dicionario como foi incluido 
        # >>> # Sort by key
        # >>> dict(sorted(people.items()))
        # {1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}
        return sorted(self.entries.keys())[::-1]

    # def delete(self, name):
    #     """
    #     Delete person with name
    #     :param name: String with name
    #     :return: return 'Numero deletado'
    #     """
    #     try:
    #         return self.entries.pop(name)
    #     except KeyError:
    #             return 'Usuario não encontrado' #6 implementada mensagem caso o nome nao esteja no dicionario


    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        name_found = False
        for item in self.entries.keys():
            if item == name:
                name_found = True
                break

        if not name_found:
            return 'Usuario não encontrado'

        return 'Numero deletado'

    def change_number(self, name, number):
        if name in self.entries:
            self.entries[name] = number
            return 'Numero alterado'
        else:
            return 'Nome não encontrado'

    def get_name_by_number(self, number):
        for name, phone_number in self.entries.items():
            if phone_number == number:
                return name
        return None

# idiomas sendo usados incorretamente linha 25 "Numero invalid"

#pb = Phonebook()
#print(pb.entries)
#pb.clear()
#pb.add(name='huginho', number='123')
#pb.add(name='zezinho', number='456')
#pb.add(name='luizinho', number='789')
#print(pb.lookup('huginho')) # retorna o numero do caboclo.
#print(pb.get_names()) #retorna os nomes dos caras da agenda
#print(pb.search('zinho'))
#print(pb.get_phonebook_sorted())

#pb.delete('zezinho')
#pb.delete('luizinho')
#pb.delete('huginho')
#pb.delete('huginho')
#print(pb.entries)