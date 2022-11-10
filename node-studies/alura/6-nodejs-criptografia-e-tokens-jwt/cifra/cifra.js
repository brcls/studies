const mensagemSecreta = 'minhamensagemsecreta';

console.log(mensagemSecreta);

function cifraMensagem(offset, mensagem) {
  let resultado = "";
  for (let i = 0; i < mensagem.length; i++) {
    let codLetraAscii = mensagem.charCodeAt(i);
    if (codLetraAscii >= 65 && codLetraAscii <= 90) {
      let calculoOffset = ((codLetraAscii - 65 + offset) % 26) + 65;
      resultado += String.fromCharCode(calculoOffset);
    } else if (codLetraAscii >= 97 && codLetraAscii <= 122) {
      let calculoOffset = ((codLetraAscii - 97 + offset) % 26) + 97;
      resultado += String.fromCharCode(calculoOffset);
    } else {
      resultado += String.fromCharCode(codLetraAscii);
    }
  }
  return resultado;
}

const mensagemCifrada = cifraMensagem(3, mensagemSecreta);

console.log(mensagemCifrada);

function decifraMensagem(offset, mensagem) {
  let resultado = "";
  for (let i = 0; i < mensagem.length; i++) {
    let codLetraAscii = mensagem.charCodeAt(i);
    if (codLetraAscii >= 65 && codLetraAscii <= 90) {
      let calculoOffset = ((codLetraAscii - 90 - offset) % 26) + 90;
      resultado += String.fromCharCode(calculoOffset);
    } else if (codLetraAscii >= 97 && codLetraAscii <= 122) {
      let calculoOffset = ((codLetraAscii - 122 - offset) % 26) + 122;
      resultado += String.fromCharCode(calculoOffset);
    } else {
      resultado += String.fromCharCode(codLetraAscii);
    }
  }
  return resultado;
}

const mensagemDecifrada = decifraMensagem(3, mensagemCifrada);

console.log(mensagemDecifrada);