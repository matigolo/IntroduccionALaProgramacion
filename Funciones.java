package aed;

import org.omg.CORBA.FloatSeqHelper;

class Funciones {

/***  Primera parte: Funciones en java ***/

    int cuadrado(int x) {
         int res = x * x;
        return res;
    }

    double distancia(double x, double y) {
        double adentro = (x * x) + (y * y);
        double res = Math.sqrt(adentro);
        

        return res;
    }

    boolean esPar(int n) {
        boolean res = n % 2 == 0;
        return res;
    }

    boolean esBisiesto(int n) {
        boolean res = ((n % 4 == 0) && (n % 100 != 0)) || (n % 400 == 0);
        return res;
    }

    int factorialIterativo(int n) {
        int i = 1;
        int res = 1;
        if (n == 0) {
            return 1;
        }

        while (n >= i) {
            res = res * i;
             i += 1;

        }

        return res;
    }

    int factorialRecursivo(int n) {
        int res = 1;
        if (n == 0) {
            return 1;
        }
        else  {
            res = n * factorialRecursivo(n-1);
        }
        return res;
    }

    boolean esPrimo(int n) {
        if (n == 0 || n == 1) {
            return false;
        }
        for (int i = 2; i < (n); i++){
            if ( n % i == 0) {
             return false;
            }
        }
        return true;
    }

    int sumatoria(int[] numeros) {
        int res = 0;
        for (int i = 0; i<= (numeros.length - 1) ; i++){
            res += numeros[i];
        }
        return res;
    }

    int busqueda(int[] numeros, int buscado) {
        for (int i = 0 ; i <= (numeros.length -1) ; i++){
            if (numeros[i] == buscado) {
                return i;
            }
        }
        return 0;
    }

    boolean tienePrimo(int[] numeros) {
        for (int i = 0; i<= (numeros.length -1); i++){
            if (esPrimo(numeros[i]) == true) {
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        for (int i = 0; i < numeros.length; i++){
            if (esPar(numeros[i]) == false){
                return false;
            }
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        if (s1.length() > s2.length()){
            return false;
        }
        for (int i = 0; i < s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i)){
                return false;
            }
        }
        
        return true;
    }

    boolean esSufijo(String s1, String s2) {
        String s1Inv = "";
        String s2Inv = "";
        for (int i=s1.length()-1; i >= 0 ; i--){
            s1Inv += s1.charAt(i);
        }
        for (int i = s2.length()-1; i>=0; i--){
            s2Inv += s2.charAt(i);
        }

        return esPrefijo(s1Inv, s2Inv);
    }

/***  Segunda parte: Debugging ***/

    boolean xor(boolean a, boolean b) {
        return (a || b) && (a != b);
    }

    boolean iguales(int[] xs, int[] ys) {
        boolean res = true;
        if (xs.length != ys.length){
            return false;
        }
        for (int i = 0; i < xs.length; i++) {
            if (xs[i] != ys[i]) {
                res = false;
            }
        }
        return res;
    }

    boolean ordenado(int[] xs) {
        boolean res = true;
        for (int i = 0; i < xs.length-1; i++) {
            if (xs[i] > xs [i+1]) {
                res = false;
            }
        }
        return res;
    }

    int maximo(int[] xs) {
        int res = xs[0];
        for (int i = 1; i <= xs.length-1; i++) {
            if (xs[i] > res) {
                res = xs[i];}
        }
        return res;
    }

    boolean todosPositivos(int[] xs) {
        boolean res = true;
        for (int x : xs) {
            if (x < 1) {
                res = false;
            }
        }
        return res;
    }

}



