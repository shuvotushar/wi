#! /bin/bash
sum=0
i="y"

echo "Primer numero: "
read n1
echo "Segundo numero: "
read n2
while [ $i = "y" ]; do
        echo
        echo "1.Sumar"
        echo "2.Restar"
        echo "3.Multiplicar"
        echo "4.Dividir"
        echo
        echo "Selecciona una opción:"
        read ch
        case $ch in
        1)
                sum=$(expr $n1 + $n2)
                echo "$n1 + $n2 = "$sum
                ;;
        2)
                sum=$(expr $n1 - $n2)
                echo "$n1 - $n2 = "$sum
                ;;
        3)
                sum=$(expr $n1 \* $n2)
                echo "$n1 × $n2 = "$sum
                ;;
        4)
                sum=$(expr $n1 / $n2)
                echo "$n1 / $n2 =  "$sum
                ;;
        *) echo "Opción invalida"
                ;;
        esac
        echo "Continuar?(y/n)"
        read i
        if [ $i != "y" ]; then
                exit
        fi
