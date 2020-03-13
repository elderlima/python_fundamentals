from testes import TestCase, main

# def somar(x, y):
#     return x + y

# def subtracao(x, y):
#     return x - y

# def multiplicacao(x, y):
#     return x * y


# assert somar(2, 2) == 4, f"Obtido: {somar(2, 2)} Esperado: 1"
# assert somar(3, 2) == 5, f"Obtido: {somar(3, 2)} Esperado: 5"

# assert subtracao(2, 2) == 0, f"Obtido: {subtracao(2, 2)} Esperado: 0"
# assert subtracao(3, 2) == 1, f"Obtido: {subtracao(3, 2)} Esperado: 1"

# assert multiplicacao(2, 2) == 4, f"Obtido: {multiplicacao(2, 2)} Esperado: 4"
# assert multiplicacao(3, 2) == 6, f"Obtido: {multiplicacao(3, 2)} Esperado: 6"

def somar(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    pass

class teste()TesteCase:

    def test_soma(self):
        self.assertEqual(somar(5, 5), 10)
        self.assertEqual(type(somar(5, 5), int))
        self.assertIsNotNone(somar(5, 5), None)
        self.asserLess(somar(5, 5), 11)

    def test_sub(self):
        self.assertEqual(subtracao(10, 5), 5)
        self.assertEqual(type(subtracao(10, 5), int))
        self.assertIsNotNone(subtracao(10, 5), None)
        self.asserLess(subtracao(10, 5), 11)

    def test_mult(self):
        self.assertEqual(somar(5, 5), 10)
        self.assertEqual(type(somar(5, 5), int))
        self.assertIsNotNone(somar(5, 5), None)
        self.asserLess(somar(5, 5), 11)

    

