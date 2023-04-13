class Programa
{
    static void Main(string[] args)
    {
        int idadeJoao = 16;
        int quantidadeDePessoas = 2;

        bool acompanhado = quantidadeDePessoas > 1;

        string textoAdicional;

        if (acompanhado)
            textoAdicional = "Joao está acompanhado";
        else
            textoAdicional = "Joao não está acompanhado";


        if (idadeJoao >= 18 || acompanhado)
        {
            Console.WriteLine(textoAdicional);
            Console.WriteLine("Pode entrar");
        }
        else
        {
            Console.WriteLine("Não pode entrar");
        }
    }
}