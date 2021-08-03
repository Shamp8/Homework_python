example = [1, 1.2, -1,True, 'Текст']
def type_for_example(el):
    for el in range(len(example)):
        print(type(example[el]))
    return
type_for_example(example)