class Programa
{
    static void Main(string[] args)
    {

        for (int contadorDeLinhas = 0; contadorDeLinhas < 10; contadorDeLinhas++)
        {
            for (int contadorDeColunas = 0; contadorDeColunas >= contadorDeLinhas; contadorDeColunas++)
            {
                Console.Write('*');
            }
            Console.WriteLine();
        }

    }
}