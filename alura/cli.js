const chalk = require("chalk");
const pegarArquivo = require("./index");

const caminho = process.argv;

async function processaTexto(caminhoDeArquivo) {
  const resultado = await pegarArquivo(caminhoDeArquivo[2]);
  console.log(chalk.yellow("Lista de links"), resultado);
}

processaTexto(caminho);
