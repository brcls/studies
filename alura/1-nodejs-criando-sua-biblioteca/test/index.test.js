const pegarArquivo = require("../index");

const arrayResult = [
  {
    FileList: "https://developer.mozilla.org/pt-BR/docs/Web/API/FileList",
  },
];

describe("pegarArquivo::", () => {
  it("deve ser uma função", () => {
    expect(typeof pegarArquivo).toBe("function");
  });
  it("deve retornar array com resultados", async () => {
    const resultado = await pegarArquivo(
      "/home/rckbrcls/Documentos/estudos/node/alura/nodejs-criando-sua-biblioteca/test/arquivos/texto1.md"
    );
    expect(resultado).toEqual(arrayResult);
  });
  it("deve retornar mensagem que 'não há links'", async () => {
    const resultado = await pegarArquivo(
      "/home/rckbrcls/Documentos/estudos/node/alura/nodejs-criando-sua-biblioteca/test/arquivos/texto-sem-link.md"
    );
    expect(resultado).toBe("não há links");
  });
  it("deve lançar um erro na falta de arquivo", async () => {
    await expect(
      pegarArquivo(
        "/home/rckbrcls/Documentos/estudos/node/alura/nodejs-criando-sua-biblioteca/test/arquivos/"
      )
    ).rejects.toThrow(/não há arquivo no caminho/);
  });
  it("deve resolver a função com sucesso", async () => {
    await expect(
      pegarArquivo(
        "/home/rckbrcls/Documentos/estudos/node/alura/nodejs-criando-sua-biblioteca/test/arquivos/texto1.md"
      )
    ).resolves.toEqual(arrayResult);
  });
});
