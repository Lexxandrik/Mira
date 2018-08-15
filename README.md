package Mira;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        System.out.println("Привет, меня зовут Mira. Представьтесь, пожалуйста.");
        System.out.println("Тебя зовут...");
        Scanner name = new Scanner(System.in);
        String str = name.nextLine();
        System.out.println("Привет, " + str);
        System.out.println("Напиши слово \"комманда\", чтобы узнать, что я умею");
        Scanner cmd = new Scanner(System.in);
        String cmd1 = cmd.next();
        
        switch (cmd1) {
        case "комманда" :
            System.out.println("1.Узнать прогноз погоды + "\n"+ 2.Последние новости");
            break;
            default : 
            System.out.println("Пока.");
            break;
        }
        

    }
}

