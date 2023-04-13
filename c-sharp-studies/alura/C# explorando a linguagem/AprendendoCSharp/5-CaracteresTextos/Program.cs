class Programa
{
    static void Main(string[] args)
    {
        char letra = 'A';
        Console.WriteLine(letra);

        letra = (char)65;
        Console.WriteLine(letra);

        letra = (char)(65 + 1);
        Console.WriteLine(letra);


        string primeiraFrase = "Alura cursos";
        Console.WriteLine(primeiraFrase + " 2022");

        string vazia = "";    
        Console.WriteLine(vazia);

        letra = ' ';
        Console.WriteLine(letra);

        string cursos = @"Cursos disponiveis:
- Go
- C
- Python";
        Console.WriteLine(cursos);
    }

}
