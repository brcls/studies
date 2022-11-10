import { createHash } from "crypto";

function criaHash(senha) {
  return createHash("sha256").update(senha).digest("hex");
}

console.log(criaHash("Uma senha qualquer"));

class Usuario {
  constructor(nome, senha) {
    this.nome = nome;
    this.hash = criaHash(senha);
  }

  autentica(nome, senha) {
    if (this.nome === nome && this.hash === criaHash(senha)) {
      console.log("Usuário autenticado com sucesso");
      return true;
    } else {
      console.log("Usuário ou senha inválidos");
      return false;
    }
  }
}


const usuario = new Usuario("João", "Uma senha qualquer");
console.log(usuario);

//caso de sucessor
usuario.autentica("João", "Uma senha qualquer");

//caso de fracasso
usuario.autentica("João", "Uma senha qualquer 2");