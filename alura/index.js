const chalk = require("chalk");
const fs = require("fs");
const path = require("path");

function extraiLinks(texto) {
  const regex = /\[([^\]]*)\]\((https?:\/\/[^$#\s].[^\s]*)\)/gm;
  const arrayResultados = [];
  let temp;

  while ((temp = regex.exec(texto)) !== null) {
    arrayResultados.push({ [temp[1]]: temp[2] });
  }

  return arrayResultados.length === 0 ? "Não há links" : arrayResultados;
}

function trataErro(erro) {
  throw new Error(chalk.red(erro.code, "não há arquivo no caminho"));
}

async function pegarArquivo(caminho) {
  const caminhoAbsoluto = path.join(__dirname, "..", caminho);
  const encoding = "utf-8";
  const arquivos = await fs.promises.readdir(caminhoAbsoluto, { encoding });
  console.log("arquivos", arquivos);
}

module.exports = pegarArquivo;
