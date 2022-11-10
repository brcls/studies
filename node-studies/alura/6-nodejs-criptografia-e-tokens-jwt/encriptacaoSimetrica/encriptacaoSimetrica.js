import { createCipheriv, randomBytes, createDecipheriv } from "crypto";

const mensagem = "Uma mensagem qualquer";
const chave = randomBytes(32);
const vi = randomBytes(16);

const cifra = createCipheriv("aes256", chave, vi);

const mensagemEncriptada =
  cifra.update(mensagem, "utf8", "hex") + cifra.final("hex");

console.log(mensagemEncriptada);

// Transmissao da mensagem encriptada - chave, vi e mensagemEncriptada

// decifração

const decifra = createDecipheriv("aes256", chave, vi);

const mensagemDecifrada = decifra.update(mensagemEncriptada, "hex", "utf8") + decifra.final("utf8");

console.log(`Mensagem decifrada: ${mensagemDecifrada}`);