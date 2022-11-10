import { createHash } from "crypto";

class Usuario {
  constructor(nome, senha) {
    this.nome = nome;
    this.hash = this.criaHash(senha);
  }

  criaHash(senha) {
    return createHash("sha256").update(senha).digest("hex");
  }

  autentica(nome, senha) {
    if (this.nome === nome && this.hash === this.criaHash(senha)) {
      console.log("Usuário autenticado com sucesso");
      return true;
    } else {
      return false;
    }
  }
}

const usuario = new Usuario("João", "1237");

for(let senhaTeste = 0; senhaTeste < 10000; senhaTeste++){
  if(usuario.autentica("João", senhaTeste.toString())){
    console.log("Senha encontrada: " + senhaTeste);
    break;
  }

}