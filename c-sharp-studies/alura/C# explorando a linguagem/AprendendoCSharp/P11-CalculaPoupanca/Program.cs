class Programa
{
    static void Main(string[] args)
    {
        double investimento = 1000;
        //int mes = 1;

        ////rendimento de 0.5% ao mês
        //while (mes <= 12)
        //{
        //    investimento = investimento + investimento * 0.005;
        //    Console.WriteLine("Mês {0}: {1}", mes, investimento);

        //    mes++;
        //}


        for (int mes = 1; mes <= 12; mes++)
        {
            investimento *= 0.005;
            Console.WriteLine("mês {0}: {1}", mes, investimento);
        }
    }
}