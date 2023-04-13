using System;
class Programa
{
    static void Main(string[] args)
    {
        Console.WriteLine("Projeto 2 - Criando variáveis");
        int idade = 27;
        Console.WriteLine("Idade: " + idade);

        idade = 27 - 5;
        Console.WriteLine(idade);
        idade = 5 * 2 - 6;
        Console.WriteLine(idade);
        idade = (5 - 2) * 3;
        Console.WriteLine(idade);

        Console.WriteLine("Tecle enter para fechar");
        Console.ReadLine();
    }

}
