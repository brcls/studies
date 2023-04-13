using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ByteBank.Titular;

namespace ByteBank.Contas
{
    public class ContaCorrente
    {
        public static int TotalDeContasCriadas { get; private set; }
        private int numero_agencia;
        public int Numero_agencia
        {
            get { return numero_agencia; }
            private set
            {
                if (value > 0)
                    this.numero_agencia = value;

            }
        }
        public string Conta { get; set; }
        public Cliente Titular { get; set; }

        private double _saldo;

        public ContaCorrente(int numero_agencia, string numero_conta)
        {
            this.Numero_agencia = numero_agencia;
            this.Conta = numero_conta;
            TotalDeContasCriadas++;
        }

        public void Depositar(double valor)
        {
            this._saldo += valor;
        }

        public bool Sacar(double valor)
        {
            if (valor <= this._saldo)
            {
                this._saldo -= valor;
                return true;
            }
            return false;
        }

        public bool Transferir(double valor, ContaCorrente destino)
        {
            if (this._saldo < valor)
            {
                return false;
            }
            if (valor < 0)
            {
                return false;
            }

            Sacar(valor);
            destino.Depositar(valor);
            return true;

        }

        public void SetSaldo(double valor)
        {
            if (valor < 0)
                return;
            else
                this._saldo = valor;
        }

        public double GetSaldo()
        { return this._saldo; }

    }
}
