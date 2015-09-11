import unittest
class TestCalculadora(unittest):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumar_de_2_mas_2(self):
        resultado = self.calc.suma(2,2)

        self.assertEqual(4, resultado)

    def test_sumar_de_3_mas_3(self):
        resultado = self.calc.suma(3,3)

        self.assertEqual(6, resultado)

    def test_sumar_de_5_mas_5(self):
        resultado = self.calc.suma(5,5)

        self.assertEqual(10, resultado)

    def tst_restar_de_4_menos_4(self):
        resultado = self.calc.resta(4,4)

        self.assertEqual(0, resultado)

    def tst_restar_de_10_menos_6(self):
        resultado = self.calc.resta(10,6)

        self.assertEqual(4, resultado)

    def tst_restar_de_14_menos_7(self):
        resultado = self.calc.resta(17,7)

        self.assertEqual(7, resultado)

class Calculadora():
    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2

if __name__=="__main__":
	unittest.main()