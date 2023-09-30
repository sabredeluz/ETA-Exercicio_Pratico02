from src.phonebook import Phonebook
import pytest

invalid_add_parameter_name = [
    ('#', '1234657890', 'Nome invalido', 'data input, name parameter = #'),
    ('@', '1234657890', 'Nome invalido', 'data input, name parameter = @'),
    ('!', '1234657890', 'Nome invalido', 'data input, name parameter = !'),
    ('$', '1234657890', 'Nome invalido', 'data input, name parameter = $'),
    ('%', '1234657890', 'Nome invalido', 'data input, name parameter = %')
]

invalid_lookup_parameter_name = [
    ('#', 'Nome invalido', 'data input, name parameter = #'),
    ('@', 'Nome invalido', 'data input, name parameter = @'),
    ('!', 'Nome invalido', 'data input, name parameter = !'),
    ('$', 'Nome invalido', 'data input, name parameter = $'),
    ('%', 'Nome invalido', 'data input, name parameter = %')
]


def test_new_instance_phonebook_should_be_one_contact():
    pb = Phonebook()
    assert len(pb.entries) == 1
    for key, value in pb.entries.items():
        assert key == 'POLICIA'
        assert value == '190'


@pytest.mark.parametrize("name, phone, expected_result, message", invalid_add_parameter_name)
def test_add_invalid_name_parameters(name, phone, expected_result, message):
    pb = Phonebook()
    actual_result = pb.add(name, phone)
    assert actual_result == expected_result, message


def test_param_phone_str_len_zero():
    # o sistema nao vai permitir uma string vazia na chave len(phone) < 0
    pb = Phonebook()
    name = 'Huguinho'
    phone = ""
    expected_result = 'Numero adicionado'
    actual_result = pb.add(name, phone)
    assert actual_result == expected_result


def test_phone_sucess_scenario():
    pb = Phonebook()
    name = 'Huguinho'
    phone = "123456789"
    expected_result = 'Numero adicionado'
    actual_result = pb.add(name, phone)
    assert actual_result == expected_result


@pytest.mark.parametrize("name, expected_result, message", invalid_lookup_parameter_name)
def test_lookup_invalid_contact(name, expected_result, message):
    pb = Phonebook()
    actual_result = pb.lookup(name)
    assert actual_result == expected_result, message


def test_lookup_default_contact():
    pb = Phonebook()
    name = 'POLICIA'
    number = '190'
    expected_result = number
    actual_result = pb.lookup(name)
    print(actual_result)
    assert actual_result == expected_result


def test_lookup_contact_sucess():
    pb = Phonebook()
    name = 'Huguinho'
    number = '123'
    pb.add(name, number)
    actual_result = pb.lookup(name)
    assert actual_result == number

def test_lookup_contact_failed():
    # lookup deveria retornar mensagem tipo telefone nao encontrado.
    # colocar
    pb = Phonebook()
    name = 'Huguinho'
    number = '123'
    expected_result = 'Name not found'
    name_not_found_in_phonebook = 'Zezinho'
    pb.add(name, number)
    actual_result = pb.lookup(name_not_found_in_phonebook)
    assert actual_result == expected_result



def test_getname_all_names():
    # TODO: validar os valores de chave no result
    pb = Phonebook()
    len_size_phone_book = 4
    pb.add(name='huguinho', number='123')
    pb.add(name='zezinho', number='456')
    pb.add(name='luizinho', number='789')
    actual_dict_size = len(pb.get_names())
    assert actual_dict_size == len_size_phone_book


def test_getnumber_all_numbers():
    pb = Phonebook()
    len_size_phone_book = 4
    pb.add(name='huguinho', number='123')
    pb.add(name='zezinho', number='456')
    pb.add(name='luizinho', number='789')
    actual_dict_size = len(pb.get_numbers())
    assert actual_dict_size == len_size_phone_book


def test_clear_message():
    pb = Phonebook()
    expected_result = 'phonebook limpado'
    pb.add(name='huguinho', number='123')
    pb.add(name='zezinho', number='456')
    pb.add(name='luizinho', number='789')
    actual_result = pb.clear()
    assert actual_result == expected_result


def test_search_1_item_sucessfull():
    searched_str = 'OLICI'
    pb = Phonebook()
    len_size_phone_book = 1
    pb.add(name='huguinho', number='123')
    pb.add(name='zezinho', number='456')
    pb.add(name='luizinho', number='789')
    actual_dict_size = len(pb.search(searched_str))
    assert actual_dict_size == len_size_phone_book


def test_search_3_items_sucessfull():
    searched_str = 'inho'
    pb = Phonebook()
    len_size_phone_book = 3
    pb.add(name='huguinho', number='123')
    pb.add(name='zezinho', number='456')
    pb.add(name='luizinho', number='789')
    actual_dict_size = len(pb.search(searched_str))
    assert actual_dict_size == len_size_phone_book


def test_get_phonebook_sorted_sucessfull():
    # sugeriu transformar o dict em list, e validar
    pb = Phonebook()
    # Huguinho, Luizinho, POLICIA, Zezinho
    pb.add(name='Huguinho', number='123')
    pb.add(name='Zezinho', number='456')
    pb.add(name='Luizinho', number='789')
    actual_result = pb.get_phonebook_sorted()
    assert 'Huguinho' == actual_result[0]
    assert 'Luizinho' == actual_result[1]
    assert 'POLICIA' == actual_result[2]
    assert 'Zezinho' == actual_result[3]


def test_get_phonebook_reverse_sucessfull():
    # sugeriu transformar o dict em list, e validar
    pb = Phonebook()
    # POLICIA, HUGUINHO, ZEZINHO, LUIZINHO
    pb.add(name='HUGUINHO', number='123')
    pb.add(name='ZEZINHO', number='456')
    pb.add(name='LUIZINHO', number='789')
    actual_result = pb.get_phonebook_reverse()
    assert 'ZEZINHO' == actual_result[0]
    assert 'POLICIA' == actual_result[1]
    assert 'LUIZINHO' == actual_result[2]
    assert 'HUGUINHO' == actual_result[3]


# def test_delete_sucessfull():
#     pb = Phonebook()
#     name = 'huguinho'
#     expected_result = 'Numero deletado'
#     pb.add(name='huguinho', number='123')
#     pb.add(name='zezinho', number='456')
#     pb.add(name='luizinho', number='789')
#     actual_result = pb.delete(name)
#     assert actual_result == expected_result


def test_delete_sucessfull():
    pb = Phonebook()
    name = 'huguinho'
    expected_result = 'Numero deletado'
    pb.add(name='huguinho', number='123')
    pb.add(name='zezinho', number='456')
    pb.add(name='luizinho', number='789')
    actual_result = pb.delete(name)
    assert actual_result == expected_result

def test_delete_not_found():
    pb = Phonebook()
    name = 'donald'
    expected_result = 'Usuario não encontrado'
    pb.add(name='huguinho', number='123')
    pb.add(name='zezinho', number='456')
    pb.add(name='luizinho', number='789')
    actual_dict_result = pb.delete(name)
    assert actual_dict_result == expected_result
