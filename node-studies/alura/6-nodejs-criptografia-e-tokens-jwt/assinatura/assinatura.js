import { generateKeyPairSync, createSign, createVerify } from "crypto";

const { publicKey, privateKey } = generateKeyPairSync("rsa", {
  modulusLength: 2048,
  publicKeyEncoding: {
    type: "spki",
    format: "pem",
  },
  privateKeyEncoding: {
    type: "pkcs8",
    format: "pem",
  },
});

let dados = "Essa string será assinada";

// Assinatura digital

const assinador = createSign("rsa-sha256");
assinador.update(dados);

const assinatura = assinador.sign(privateKey, "hex");

console.log(`Assinatura: ${assinatura}`);

// Intermediário

dados += " e essa string não";

// Envio desse documento

// Verificação da assinatura

const verificador = createVerify("rsa-sha256");
verificador.update(dados);

const verificacao = verificador.verify(publicKey, assinatura, "hex");

console.log(`Verificação: ${verificacao}`);
