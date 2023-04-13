class Programa
{
    static void Main(string[] args)
    {
        int idadeJoao = 16;
        int quantidadeDePessoas = 2;

        if (idadeJoao >= 18)
        {
            Console.WriteLine("Pode entrar");
        }
        else
        {
            if (quantidadeDePessoas > 1)
            {
                Console.WriteLine("Ele está acompanhado! Pode entrar");
            }
            else
            {
                Console.WriteLine("Não pode entrar");
            }
        }
    }
}