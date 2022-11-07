import { somaHorasExtras, calculaDescontos } from '../index';

describe('Testes dos cálculos de folha', () => {
  it('Deve retornar a soma das horas extras', () => {
    const esperado = 2500;
    const retornado = somaHorasExtras(2000, 500);

    expect(retornado).toBe(esperado);
  });

  it('Deve descontar o valor do salario', () => {
    const esperado = 2000;
    const retornado = calculaDescontos(2500, 500);

    expect(retornado).toBe(esperado);
  });
});

// const verifiqueSe = (valor) => {
//   const assercoes = {
//     ehEexatamenteIgualA(esperado) {
//       if (valor !== esperado) {
//         throw new Error(
//           `O valor esperado era ${esperado}, mas o recebido foi ${valor}`,
//         );
//       }
//     },
//   };
//   return assercoes;
// };

// const teste = (titulo, funcaoDeTeste) => {
//   try {
//     funcaoDeTeste();
//     console.log(`✔ ${titulo}`);
//   } catch {
//     console.log(`✖ ${titulo}`);
//   }
// };

// teste('somaHorasExtras', () => {
//   const esperado = 2500;
//   const retornado = somaHorasExtras(2000, 500);

//   verifiqueSe(retornado).ehEexatamenteIgualA(esperado);
// });

// teste('calculaDesconto', () => {
//   const esperado = 2300;
//   const retornado = calculaDescontos(2500, 200);

//   verifiqueSe(retornado).ehEexatamenteIgualA(esperado);
// });
