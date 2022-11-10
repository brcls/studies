import jwt from "jsonwebtoken";

const chaveSecreta = "minha-chave-secreta";

const token = jwt.sign(
  { apelido: "jm", curso: "segurança e nodejs" },
  chaveSecreta,
);

console.log(token);

const tokenDecodificado = jwt.verify(token, chaveSecreta);

console.log(tokenDecodificado);