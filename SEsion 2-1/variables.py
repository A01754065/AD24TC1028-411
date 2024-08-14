"""
inicio;
recibir número;
if(n es negativo y n es impar)
{
  imprimo que es impar negativo;
}
else
{
  if(n positivo y n espar)
  {
   imprimo es par positivo; 
  }
  else
  {
    if(n es negativo y n es par)
    {
      imprimo es par negativo;
    }  
    else
    {
      imprimo impar positivo;
    }
}
}

fin;
"""
numero = int(input("Dame un número: "))
if (numero < = 0 and numero %2 != 0):
    print("Número es impar negativo: ")

else: 
    if (numero > 0 and numero%2 == 0 ):
        
